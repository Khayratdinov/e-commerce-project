from django.forms import ModelForm

# ============================================================================ #
from project.apps.blog.models import BlogComment


# =============================== COMMENT BLOG =============================== #


class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ["name", "phone", "email", "comment"]
