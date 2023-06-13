from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import (
    TabbedTranslationAdmin,
    TabbedExternalJqueryTranslationAdmin,
)


# ============================================================================ #
from project.apps.book.models import (
    Category,
    Tag,
    Book,
    BookSlider,
    BookComment,
    CollectionBook,
    CollectionSlider,
)


class CategoryAdmin(TabbedTranslationAdmin):
    list_display = [
        "title",
    ]
    exclude = [
        "slug",
    ]
    list_per_page = 20


class TagAdmin(TabbedTranslationAdmin):
    list_display = [
        "title",
    ]
    exclude = [
        "slug",
    ]
    list_per_page = 20


class CollectionSliderInline(admin.TabularInline):
    model = CollectionSlider
    extra = 0


class CollectionBookAdmin(TabbedTranslationAdmin):
    inlines = [
        CollectionSliderInline,
    ]
    list_display = (
        "title_uz",
        "status",
        "created_at",
        "special_status",
    )
    list_per_page = 20
    list_editable = [
        "special_status",
        "status",
    ]
    list_filter = [
        "status",
        "special_status",
    ]
    exclude = [
        "slug",
    ]


class BookCommentAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "user",
        "rate",
        "comment",
        "status",
        "created_at",
    )
    list_filter = (
        "book",
        "user",
        "status",
    )
    search_fields = (
        "book",
        "user",
        "comment",
    )
    list_editable = ["status"]
    list_per_page = 20


class Book_CommentInline(admin.TabularInline):
    model = BookComment
    extra = 0


class Book_sliderInline(admin.TabularInline):
    model = BookSlider
    extra = 0


class BookAdmin(TabbedTranslationAdmin):
    inlines = [
        Book_sliderInline,
        Book_CommentInline,
    ]
    list_display = (
        "title_uz",
        "status",
        "created_at",
    )
    search_fields = ("title_uz",)
    list_per_page = 20
    list_editable = ["status"]
    list_filter = ["category", "tags"]
    prepopulated_fields = {"slug": ("title_uz",)}
    readonly_fields = ["rating", "count_comment"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "detail",
                )
            },
        ),
        (
            "Umimiy malumotlar",
            {
                "fields": (
                    "coverpage",
                    ("price", "discount_price"),
                    (
                        "author",
                        "isbn",
                        "language",
                        "date_published",
                        "publisher",
                    ),
                    ("rating", "count_comment"),
                )
            },
        ),
        (
            "Kitob statusi",
            {
                "fields": (("status", "sales_status"),),
            },
        ),
        (
            "Bir biri bilan bolgliq bolgan malumot turlari",
            {
                "fields": (
                    "category",
                    "collection_book",
                    "tags",
                ),
            },
        ),
        (
            "O`zgartilmasin",
            {
                "fields": ("slug",),
                "description": "Bul jer ozgertilmesin bul jer ozi avto toltiriladi",
                "classes": ("collapse",),
            },
        ),
    )


# ======================== REGISTER YOUR MODELS HERE. ======================== #
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(BookSlider)
admin.site.register(BookComment, BookCommentAdmin)
admin.site.register(CollectionBook, CollectionBookAdmin)