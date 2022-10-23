from django.db import models
from django.db.models import Count
from django.urls import reverse

# ============================================================================ #
from project.apps.common.models import BaseModel

# ============================================================================ #
#                                     BLOG                                     #
# ============================================================================ #


class Blog(BaseModel):

    STATUS = (
        ("True", "Published"),
        ("False", "Not Published"),
    )

    title = models.CharField(max_length=355)
    image = models.ImageField(upload_to="images/")

    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default="True")
    category = models.ForeignKey("Category_Blog", on_delete=models.CASCADE)
    views = models.PositiveBigIntegerField(default=0)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})


# ============================================================================ #


class Category_Blog(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_blog_detail", kwargs={"slug": self.slug})


# ============================================================================ #


class Comment_blog(BaseModel):

    STATUS = (
        ("True", "No Block"),
        ("False", "Block"),
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField(max_length=355, blank=False)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default="True")

    def __str__(self):
        return self.name
