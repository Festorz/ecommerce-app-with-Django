from django.contrib import admin

from .models import Item, User


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'user',
                    'price',
                    'discount_price',
                    'category',
                    'quantity',
                    'sold',
                    'ordered',
                    ]


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'fullname']


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(User, UserAdmin)
