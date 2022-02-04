from django import template

from ..models import *

register = template.Library()

@register.inclusion_tag('baseapp/category.html')
def show_category():
    categories = Category.objects.all()
    return {
        'categories': categories,
    }
