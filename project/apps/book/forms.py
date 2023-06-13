from django.forms import ModelForm

# ============================================================================ #
from project.apps.book.models import BookComment


# ============================= BOOK COMMENT FORM ============================ #


class BookCommentForm(ModelForm):
    class Meta:
        model = BookComment
        fields = ["rate", "comment"]