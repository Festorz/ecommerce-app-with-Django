from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from Commerce.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'title',
            'price',
            'discount_price',
            'category',
            'quantity',
            'description',
            'image',
        )


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'price',
            'discount_price',
            'quantity',
        )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254)
    phone = forms.CharField(required=True, max_length=13)
    fullname = forms.CharField(required=True, max_length=100)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'fullname',
            'phone',
            'location',
            'profile_picture',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']
        user.phone = self.cleaned_data['location']
        user.email = self.cleaned_data['email']
        user.fullname = self.cleaned_data['fullname']

        if commit:
            user.save()

        return user


class UserForm(forms.Form):
    phone = forms.CharField(required=False)
    use_default_phone = forms.BooleanField(required=False)
    use_new_phone = forms.BooleanField(required=False)
