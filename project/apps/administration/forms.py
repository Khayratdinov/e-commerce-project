from django import forms
from django.forms import (
    ModelForm,
    TextInput,
    FileInput,
    NumberInput,
    SelectMultiple,
)

# ============================================================================ #
from project.apps.book.models import Category, Book, BookSlider

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


# ================================ BOOK SLIDER =============================== #


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
