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
from project.apps.book.models import Category, Book, BookSlider, Tag, BookComment
from project.apps.common.models import HomeSlider
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

        widgets = {
            "title_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Category Uzb tilida"}
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
            "category",
            "author",
            "status",
            "sales_status",
            "tags",
        ]

        widgets = {
            "title_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "detail_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "detail_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter detail"}
            ),
            "coverpage": FileInput(
                attrs={"class": "form-control", "placeholder": "Enter image"}
            ),
            "price": NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter price"}
            ),
            "author": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter author"}
            ),
            "category": SelectMultiple(
                attrs={"class": "form-control", "placeholder": "Enter category"}
            ),
            "tags": SelectMultiple(
                attrs={"class": "form-control", "placeholder": "Enter tags"}
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

        widgets = {
            "title_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
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
            "shape",
            "cover",
        ]
        widgets = {
            "title_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_ru": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "title_en": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "description_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter description"}
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
            "shape": FileInput(
                attrs={"class": "form-control", "placeholder": "Enter shape"}
            ),
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
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "price": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter price"}
            ),
            "wight": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter wight"}
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
        widgets = {
            "title_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
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
        widgets = {
            "title_uz": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
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
                attrs={"class": "form-control", "placeholder": "Enter image"}
            ),
            "text_uz": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter text"}
            ),
            "text_ru": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter text"}
            ),
            "text_en": CKEditorWidget(
                attrs={"class": "form-control", "placeholder": "Enter text"}
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
