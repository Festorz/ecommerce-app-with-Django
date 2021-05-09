import random
import string

from django.conf import settings
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import Q
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('C', 'Clothing'),
    ('F', 'Furniture'),
    ('E', 'Electronics'),
    ('Fd', 'Foodstuff'),
    ('R', 'Rentals'),
)


def create_slug_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query) |
                         Q(slug__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone, fullname, profile_picture, password, location):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, fullname=fullname,
                          profile_picture=profile_picture, location=location)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, phone, password, location, fullname=None, profile_picture=None):
        user = self.create_user(username=username, email=email, phone=phone, fullname=fullname, password=password,
                                profile_picture=profile_picture, location=location)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    phone = models.CharField(max_length=13, blank=False)
    fullname = models.CharField(max_length=70, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile', default='')
    location = models.CharField(max_length=100, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["email", "phone"]
    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return self.username


class Item(models.Model):
    title = models.CharField(max_length=settings.COMMERCE_TITLE_MAX_LENGTH)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField(blank=False, default=create_slug_code)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    sold = models.IntegerField(default=0)
    description = models.TextField(default='Provide a description.....')
    image = models.ImageField(upload_to='items')

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('commerce:products', kwargs=kwargs)

    def get_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('commerce:edit_product', kwargs=kwargs)

    def get_seller_profile(self):
        return reverse('commerce:view_seller', kwargs={
            'user': self.user
        })

    def contact_seller(self):
        return reverse('commerce:view_seller', kwargs={
            'user': self.user
        })

    def get_view_item_url(self):
        return reverse('commerce:product', kwargs={
            'category': self.category
        })

    def get_remove_item(self):
        return reverse('commerce:remove_product', kwargs={'slug': self.slug})

    def get_quantity(self):
        return self.quantity
