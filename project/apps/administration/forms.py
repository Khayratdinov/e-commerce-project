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
        fields = ["title"]

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Category"}
            ),
        }


# ================================= BOOK FORM ================================ #


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "detail",
            "coverpage",
            "price",
            "author",
            "category",
            "tags",
            "status",
            "sales_status",
        ]

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "detail": TextInput(
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
            "publisher": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter publisher"}
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
