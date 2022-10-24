from django.contrib import admin

# ============================================================================ #
from project.apps.blog.models import Blog, Category_Blog, Comment_blog


# ======================== REGISTER YOUR MODELS HERE. ======================== #
admin.site.register(Blog)
admin.site.register(Category_Blog)
admin.site.register(Comment_blog)
