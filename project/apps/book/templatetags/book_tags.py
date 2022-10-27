from django import template

# ============================================================================ #
from project.apps.book.models import Category


register = template.Library()


@register.simple_tag(name="get_categories")
def get_categories():
    category_list = Category.objects.all()
    return category_list


@register.simple_tag(name="categories")
def categories():
    category_list = Category.objects.all()
    return category_list
