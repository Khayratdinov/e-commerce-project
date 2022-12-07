from django import template

# ============================================================================ #
from project.apps.blog.models import CategoryBlog, Blog, BlogComment

register = template.Library()


@register.simple_tag(name="get_categories")
def get_categories():
    return CategoryBlog.objects.all()
