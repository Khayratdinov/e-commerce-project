from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import (
    TabbedTranslationAdmin,
)

# ============================================================================ #
from project.apps.blog.models import Blog, CategoryBlog, BlogComment


class CategoryBlogAdmin(TabbedTranslationAdmin):
    list_display = [
        "title",
    ]
    exclude = [
        "slug",
    ]


# class BlogCommentInline(admin.TabularInline):
#     model = BlogComment
#     extra = 0


class BlogAdmin(TabbedTranslationAdmin):
    # inlines = [
    #     BlogCommentInline,
    # ]
    list_display = (
        "title_uz",
        "status",
        "created_at",
    )
    exclude = [
        "slug",
    ]
    search_fields = ("title_uz",)
    list_per_page = 20
    list_editable = ["status"]
    list_filter = ["category", "status"]


# ======================== REGISTER YOUR MODELS HERE. ======================== #
admin.site.register(Blog, BlogAdmin)
admin.site.register(CategoryBlog, CategoryBlogAdmin)
# admin.site.register(BlogComment)