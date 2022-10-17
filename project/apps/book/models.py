from django.db import models
from django.urls import reverse

# ============================================================================ #
from project.apps.common.models import BaseModel


# Create your models here.

# =============================== CATEGORY BOOK ============================== #


class Category(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title


# ==================================== TAG =================================== #


class Tag(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title


# =================================== BOOK =================================== #


class Book(BaseModel):

    STATUS = (
        ("True", "Published"),
        ("False", "Not Published"),
    )

    SALES_STATUS = (
        ("CHEGIRMA", "CHEGIRMA"),
        ("YANGI", "YANGI"),
        ("FALSE", "FALSE"),
    )
    title = models.CharField(max_length=200, unique=True)
    detail = models.TextField()
    coverpage = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.CharField(max_length=100, blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True, related_name="book")
    tags = models.ManyToManyField(Tag, blank=True, related_name="book")
    status = models.CharField(max_length=10, choices=STATUS, default="True")
    sales_status = models.CharField(
        max_length=15, choices=SALES_STATUS, default="False"
    )
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})


# ================================ BOOK SLIDER =============================== #


class BookSlider(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
