import math

# ============================================================================ #

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import Avg, Count

# ============================================================================ #
from project.apps.common.models import BaseModel


# Create your models here.

User = get_user_model()


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
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def avaregereview(self):
        reviews = BookComment.objects.filter(book=self, status="True").aggregate(
            avarage=Avg("rate")
        )
        avg = 0
        if reviews["avarage"] is not None:
            avg = math.ceil((reviews["avarage"]))
        return avg

    def countreview(self):
        reviews = BookComment.objects.filter(book=self, status="True").aggregate(
            count=Count("id")
        )
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


# ================================ BOOK SLIDER =============================== #


class BookSlider(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")


# =============================== BOOK COMMENT =============================== #


class BookComment(BaseModel):

    STATUS = (
        ("True", "Published"),
        ("False", "Not Published"),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default="True")

    def __str__(self):
        return self.book.title
