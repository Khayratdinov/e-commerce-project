from django.contrib import admin

# ============================================================================ #
from project.apps.blog.models import Blog, CategoryBlog, BlogComment


# ======================== REGISTER YOUR MODELS HERE. ======================== #
admin.site.register(Blog)
admin.site.register(CategoryBlog)
admin.site.register(BlogComment)
