from django.forms import (
    ModelForm,
    TextInput,
)

# ============================================================================ #
from project.apps.book.models import Category

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
