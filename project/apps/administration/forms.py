from django import forms
from django.contrib.auth import get_user_model
from django.forms import (
    ModelForm,
    TextInput,
    FileInput,
    NumberInput,
    SelectMultiple,
)

# ============================================================================ #
from ckeditor.widgets import CKEditorWidget

# ============================================================================ #
from project.apps.book.models import (
    Category,
    Book,
    BookSlider,
    Tag,
    BookComment,
    CollectionBook,
    CollectionSlider,
)
from project.apps.common.models import (
    HomeSlider,
    HeadImages,
    CommonInfo,
    FAQ,
    About,
    ShippingInfo,
    PaymentInfo,
    DiscountInfo,
)
from project.apps.order.models import Shipping
from project.apps.administration.models import ShopCart
from project.apps.blog.models import CategoryBlog, Blog


User = get_user_model()

# ============================================================================ #
#                                   BOOK APP                                   #
# ============================================================================ #

# ============================ CATEGORY BOOK FORM ============================ #


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["title_uz", "title_ru", "title_en"]

        labels = {
            "title_uz": "Kitob Kategoriyasi nomi o`zbek tilida",
            "title_ru": "Kitob Kategoriyasi nomi rus tilida",
            "title_en": "Kitob Kategoriyasi nomi ingliz tilida",
        }

        widgets = {
            "title_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Category Uzb tilida",
                }
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Category Rus tilida"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Category Eng tilida"}
            ),
        }


# ================================= BOOK FORM ================================ #


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title_uz",
            "title_ru",
            "title_en",
            "detail_uz",
            "detail_ru",
            "detail_en",
            "coverpage",
            "price",
            "discount_price",
            "author",
            "isbn",
            "language",
            "date_published",
            "publisher",
            "category",
            "tags",
            "collection_book",
            "status",
            "sales_status",
        ]

        labels = {
            "title_uz": "Kitob nomi o`zbek tilida",
            "title_ru": "Kitob nomi rus tilida",
            "title_en": "Kitob nomi ingliz tilida",
            "detail_uz": "Kitob haqqida malumot o`zbek tilida",
            "detail_ru": "Kitob haqqida malumot rus tilida",
            "detail_en": "Kitob haqqida malumot ingliz tilida",
            "coverpage": "Kitob rasmi",
            "price": "Kitob narxi",
            "discount_price": "Chegirma %",
            "publisher": "Kim tomonidan nashr qilingan",
            "category": "Kitob cateogoriyasi",
            "author": "Kitob mualifi",
            "isbn": "Kitobning ISBN raqami",
            "language": "Kitob qaysi tilda",
            "date_published": "Kitob qashon shiqarilgan",
            "status": "Kitob mavjudligi",
            "sales_status": "Kitob holati",
            "tags": "Kitob uchin kalit sozlar",
            "collection_book": "Kitoblar toplami",
        }

        widgets = {
            "title_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter title",
                }
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control mb-5", "placeholder": "Enter title"}
            ),
            "detail_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter detail",
                }
            ),
            "detail_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "coverpage": FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter image",
                }
            ),
            "price": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter price",
                    "required": True,
                }
            ),
            "discount_price": NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter price"}
            ),
            "author": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter author"}
            ),
            "isbn": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter isbn"}
            ),
            "language": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter language"}
            ),
            "date_published": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter date_published"}
            ),
            "publisher": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter publisher"}
            ),
            "category": SelectMultiple(
                attrs={
                    "class": "multiple-select",
                    "placeholder": "Enter category",
                    "data-placeholder": "multiple",
                    "placeholder": "Enter publisher",
                    "required": True,
                }
            ),
            "tags": SelectMultiple(
                attrs={
                    "class": "multiple-select",
                    "multiple": "multiple",
                    "placeholder": "Enter tags",
                }
            ),
            "collection_book": SelectMultiple(
                attrs={
                    "class": "multiple-select",
                    "multiple": "multiple",
                    "placeholder": "Enter collection_book",
                }
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
            "sales_status": forms.Select(attrs={"class": "form-select"}),
        }


# ============================= BOOK SLIDER FORM ============================= #


class BookSliderForm(ModelForm):
    class Meta:
        model = BookSlider
        fields = ["book", "image"]

        widgets = {
            "book": forms.Select(attrs={"class": "form-control"}),
            "image": FileInput(
                attrs={"class": "form-control", "placeholder": "Enter image"}
            ),
        }


# ============================ TAGS FORM FOR BOOK ============================ #


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["title_uz", "title_ru", "title_en"]

        labels = {
            "title_uz": "Kitob kalit soz nomi o`zbek tilida",
            "title_ru": "Kitob kalit soz nomi rus tilida",
            "title_en": "Kitob kalit soz nomi ingliz tilida",
        }

        widgets = {
            "title_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter title",
                }
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
        }


# ============================================================================ #


# =============================== BOOK COMMENT =============================== #


class BookCommentForm(ModelForm):
    class Meta:
        model = BookComment
        fields = ["status"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# ================================ HOME SLIDER =============================== #


class HomeSliderForm(ModelForm):
    class Meta:
        model = HomeSlider
        fields = [
            "title_uz",
            "title_ru",
            "title_en",
            "description_uz",
            "description_ru",
            "description_en",
            "status",
            "url",
            "cover",
        ]
        widgets = {
            "title_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter title",
                }
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "description_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter description",
                }
            ),
            "description_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "url": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter url"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
            "cover": FileInput(
                attrs={"class": "form-control", "placeholder": "Enter cover"}
            ),
        }


# ================================= SHIPPING ================================= #


class ShippingForm(ModelForm):
    class Meta:
        model = Shipping
        fields = ["title", "price", "wight"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter title",
                }
            ),
            "price": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter price",
                }
            ),
            "wight": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter wight",
                }
            ),
        }


# ============================== USER EDIT FORM ============================== #


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "is_active",
            "is_staff",
            "is_superuser",
        ]
        widgets = {
            "is_active": forms.CheckboxInput(
                attrs={"class": "form-check-input", "id": "flexSwitchCheckChecked"}
            ),
            "is_staff": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


# ============================== ADD TO SHOPCART ============================= #


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ["quantity"]


# =============================== CATEGORY BLOG ============================== #


class CategoryBlogForm(ModelForm):
    class Meta:
        model = CategoryBlog
        fields = [
            "title_uz",
            "title_ru",
            "title_en",
        ]
        labels = {
            "title_uz": "Category Blog nomi o`zbek tilida",
            "title_ru": "Category Blog nomi rus tilida",
            "title_en": "Category Blog nomi ingliz tilida",
        }
        widgets = {
            "title_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter title",
                }
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
        }


# ================================= BLOG FORM ================================ #


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title_uz",
            "title_ru",
            "title_en",
            "description_uz",
            "description_ru",
            "description_en",
            "text_uz",
            "text_ru",
            "text_en",
            "image",
            "category",
            "status",
        ]

        labels = {
            "title_uz": "Blog nomi o`zbek tilida",
            "title_ru": "Blog nomi rus tilida",
            "title_en": "Blog nomi ingliz tilida",
            "description_uz": "Blog haqqida qisqacha malumot o`zbek tilida",
            "description_ru": "Blog haqqida qisqacha malumot rus tilida",
            "description_en": "Blog haqqida qisqacha malumot ingliz tilida",
            "text_uz": "Blog haqqida malumot o`zbek tilida",
            "text_ru": "Blog haqqida malumot rus tilida",
            "text_en": "Blog haqqida malumot ingliz tilida",
            "image": "Blog rasmi",
            "status": "Blog mavjudligi",
        }
        widgets = {
            "title_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter title",
                }
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "description_uz": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_ru": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_en": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "image": FileInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter image",
                }
            ),
            "text_uz": CKEditorWidget(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter text",
                }
            ),
            "text_ru": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter text"}
            ),
            "text_en": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter text"}
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                    "required": True,
                }
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# ========================== RANDOMBRADCAUMPIMG FORM ========================= #


class RandomBradcaumpImgForm(ModelForm):
    class Meta:
        model = HeadImages
        fields = ["image", "status"]
        widgets = {
            "image": FileInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter image",
                }
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# ================================== SETTING ================================= #


class CommonInfoForm(ModelForm):
    class Meta:
        model = CommonInfo
        fields = [
            "description_contact_uz",
            "description_contact_ru",
            "description_contact_en",
            "description_footer_uz",
            "description_footer_ru",
            "description_footer_en",
            "logo",
            "phone",
            "email",
            "address",
            "instagram",
            "telegram",
            "facebook",
            "status",
        ]

        labels = {
            "description_contact_uz": "Contact pagega malumot o`zbek tilida",
            "description_contact_ru": "Contact pagega malumot rus tilida",
            "description_contact_en": "Contact pagega malumot  ingliz tilida",
            "description_footer_uz": "Footer bolimiga malumot o`zbek tilida",
            "description_footer_ru": "Footer bolimiga malumot rus tilida",
            "description_footer_en": "Footer bolimiga malumot ingliz tilida",
            "logo": "Logo",
            "phone": "Telefon raqam",
            "email": "Email manzil",
            "address": "Toliq manzil",
            "instagram": "Instagram account",
            "facebook": "facebook account",
            "telegram": "telegram account",
            "status": "Status",
        }
        widgets = {
            "description_contact_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_contact_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_contact_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_footer_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_footer_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "description_footer_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "logo": FileInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter image",
                }
            ),
            "phone": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter phone"}
            ),
            "email": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter email"}
            ),
            "address": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter address"}
            ),
            "instagram": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter url"}
            ),
            "telegram": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter url"}
            ),
            "facebook": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter url"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# ============================== COLLECTION BOOK ============================= #


class CollectionBookForm(ModelForm):
    class Meta:
        model = CollectionBook
        fields = [
            "title_uz",
            "title_ru",
            "title_en",
            "description_uz",
            "description_ru",
            "description_en",
            "body_uz",
            "body_ru",
            "body_en",
            "price",
            "image",
            "status",
            "special_status",
        ]

        labels = {
            "title_uz": " 🇺🇿 Collection Book nomi o`zbek tilida 🔴",
            "title_ru": " 🇷🇺 Collection Book nomi rus tilida",
            "title_en": " 🇺🇸 Collection Book nomi ingliz tilida",
            "description_uz": " 🇺🇿 Collection Book qisqacha malumot o`zbek tilida 🔴",
            "description_ru": " 🇷🇺 Collection Book qisqacha malumot rus tilida",
            "description_en": " 🇺🇸 Collection Book qisqacha malumot ingliz tilida",
            "body_uz": " 🇺🇿 Collection Book toliq malumot ingliz tilida 🔴",
            "body_ru": " 🇷🇺 Collection Book toliq malumot ingliz tilida",
            "body_en": " 🇺🇸 Collection Book toliq malumot ingliz tilida",
            "price": "Collection Book Narxi 🔴",
            "image": "Collection Book rasmi 🔴",
            "status": "Collection Book mavjudligi",
            "special_status": "Maqsus toplammi ?",
        }
        widgets = {
            "title_uz": TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter title",
                }
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "description_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description_uz"}
            ),
            "description_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description_ru"}
            ),
            "description_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description_en"}
            ),
            "body_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter body_uz"}
            ),
            "body_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter body_ru"}
            ),
            "body_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter body_en"}
            ),
            "price": NumberInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Enter price",
                }
            ),
            "image": FileInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Images",
                }
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
            "special_status": forms.Select(attrs={"class": "form-select"}),
        }


# ============================= COLLECTION SLIDER ============================ #


class CollectionSliderForm(ModelForm):
    class Meta:
        model = CollectionSlider
        fields = ["collection", "image"]

        widgets = {
            "collection": forms.Select(attrs={"class": "form-control"}),
            "image": FileInput(
                attrs={"class": "form-control", "placeholder": "Enter image"}
            ),
        }


# ==================================== FAQ =================================== #


class FaqForm(ModelForm):
    class Meta:
        model = FAQ
        fields = ["question", "answer", "status"]

        widgets = {
            "question": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter question"}
            ),
            "answer": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter answer"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# =================================== ABOUT ================================== #


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = ["detail_uz", "detail_ru", "detail_en", "status"]

        labels = {
            "detail_uz": "Biz haqqimizda malumot o`zbek tilida",
            "detail_ru": "Biz haqqimizda malumot rus tilida",
            "detail_en": "Biz haqqimizda malumot ingliz tilida",
        }

        widgets = {
            "detail_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# ============================================================================ #


# ================================= SHIPPING ================================= #


class ShippingInfoForm(ModelForm):
    class Meta:
        model = ShippingInfo
        fields = ["detail_uz", "detail_ru", "detail_en", "status"]

        labels = {
            "detail_uz": "Etkazip berish xizmatlari haqqida o`zbek tilida",
            "detail_ru": "Etkazip berish xizmatlari haqqida rus tilida",
            "detail_en": "Etkazip berish xizmatlari haqqida ingliz tilida",
        }

        widgets = {
            "detail_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# ============================================================================ #

# ================================ PAYMENTINFO =============================== #


class PaymentInfoForm(ModelForm):
    class Meta:
        model = PaymentInfo
        fields = ["detail_uz", "detail_ru", "detail_en", "status"]

        labels = {
            "detail_uz": "Tolov tizimi  haqqida o`zbek tilida",
            "detail_ru": "Tolov tizimi haqqida rus tilida",
            "detail_en": "Tolov tizimi haqqida ingliz tilida",
        }

        widgets = {
            "detail_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


# ============================================================================ #

# =============================== DISCOUNTINFO =============================== #


class DiscountInfoForm(ModelForm):
    class Meta:
        model = DiscountInfo
        fields = ["detail_uz", "detail_ru", "detail_en", "status"]

        labels = {
            "detail_uz": "Chegirmalar  haqqida o`zbek tilida",
            "detail_ru": "Chegirmalar haqqida rus tilida",
            "detail_en": "Chegirmalar haqqida ingliz tilida",
        }

        widgets = {
            "detail_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
        }