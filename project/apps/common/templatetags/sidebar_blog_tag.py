from django import template

# ============================================================================ #
from project.apps.blog.models import CategoryBlog, Blog, BlogComment

register = template.Library()


@register.simple_tag(name="get_categories")
def get_categories():
    return CategoryBlog.objects.all()


@register.simple_tag(name="get_blog_recent")
def get_blog_recent():
    return Blog.objects.filter(status="True").order_by("-created_at")[:3]


@register.simple_tag(name="get_blog_comment")
def get_blog_comment():
    return BlogComment.objects.filter(status="True").order_by("-created_at")[:5]
