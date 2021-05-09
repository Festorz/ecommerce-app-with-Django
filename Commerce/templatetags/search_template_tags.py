from django import template
from Commerce.models import Item


register = template.Library()

@register.filter
def class_name(value):
    return value.__class__.__name__
