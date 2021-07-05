from django import template
from InfoBlog.models import *

register = template.Library()

@register.simple_tag(name='get_categories')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('InfoBlog/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {"categories": categories, "category_selected": category_selected}