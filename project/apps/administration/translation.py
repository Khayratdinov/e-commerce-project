from modeltranslation.translator import translator, TranslationOptions

# ============================================================================ #
from project.apps.book.models import Book, Category, Tag, CollectionBook
from project.apps.blog.models import Blog, CategoryBlog
from project.apps.common.models import (
    HomeSlider,
    CommonInfo,
    About,
    ShippingInfo,
    PaymentInfo,
    DiscountInfo,
)

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


class CollectionBookTranslationOptions(TranslationOptions):
    fields = ("title", "description", "body")


class AboutTranslationOptions(TranslationOptions):
    fields = ("detail",)


class ShippingInfoTranslationOptions(TranslationOptions):
    fields = ("detail",)


class PaymentInfoTranslationOptions(TranslationOptions):
    fields = ("detail",)


class DiscountInfoTranslationOptions(TranslationOptions):
    fields = ("detail",)


# ============================================================================ #
#                                   REGISTER                                   #
# ============================================================================ #

translator.register(Book, BookTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(CollectionBook, CollectionBookTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(CategoryBlog, CategoryBlogTranslationOptions)
translator.register(HomeSlider, HomeSliderTranslationOptions)
translator.register(CommonInfo, CommonInfoTranslationOptions)

translator.register(About, AboutTranslationOptions)
translator.register(ShippingInfo, ShippingInfoTranslationOptions)
translator.register(PaymentInfo, PaymentInfoTranslationOptions)
translator.register(DiscountInfo, DiscountInfoTranslationOptions)