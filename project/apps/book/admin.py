from django.contrib import admin

# ============================================================================ #
from project.apps.book.models import Category, Tag, Book, BookSlider, BookComment


# ======================== REGISTER YOUR MODELS HERE. ======================== #
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(BookSlider)
admin.site.register(BookComment)
