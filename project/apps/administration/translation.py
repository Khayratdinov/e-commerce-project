from modeltranslation.translator import translator, TranslationOptions

# ============================================================================ #
from project.apps.book.models import Book, Category, Tag
from project.apps.blog.models import Blog, CategoryBlog
from project.apps.common.models import HomeSlider, CommonInfo

# ============================================================================ #


# ========================== BOOK TRANSLATIONOPTIONS ========================= #


class BookTranslationOptions(TranslationOptions):
    fields = ("title", "detail")


# ======================== CATEGORY TRANSLATIONOPTIONS ======================= #


class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


# ========================== TAG TRANSLATIONOPTIONS ========================== #


class TagTranslationOptions(TranslationOptions):
    fields = ("title",)


# ========================= BLOG TRANSLATION OPTIONS ========================= #


class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "description", "text")


# ======================== CATEGORY TRANSLATIONOPTIONS ======================= #


class CategoryBlogTranslationOptions(TranslationOptions):
    fields = ("title",)


# ====================== HOME SLIDER TRANSLATIONOPTIONS ====================== #


class HomeSliderTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )


# ======================= COMMONINFO TRANSLATIONOPTIONS ====================== #


class CommonInfoTranslationOptions(TranslationOptions):
    fields = (
        "description_contact",
        "description_footer",
    )


# ============================================================================ #
#                                   REGISTER                                   #
# ============================================================================ #

translator.register(Book, BookTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(CategoryBlog, CategoryBlogTranslationOptions)
translator.register(HomeSlider, HomeSliderTranslationOptions)
translator.register(CommonInfo, CommonInfoTranslationOptions)
