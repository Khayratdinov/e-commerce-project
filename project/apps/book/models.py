import math


# ============================================================================ #

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import Avg, Count

# ============================================================================ #
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from slugify import slugify


# ============================================================================ #
from project.apps.common.models import BaseModel


# Create your models here.

User = get_user_model()


# =============================== CATEGORY BOOK ============================== #


class Category(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=350, null=False, unique=True)

    class Meta:
        verbose_name = "2. Kitob kategoriyasi"
        verbose_name_plural = "2. Kitoblar kategoriyasi"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz)
        super(Category, self).save(*args, **kwargs)


# ==================================== TAG =================================== #


class Tag(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Kalit so`z nomi")
    slug = models.SlugField(max_length=350, null=False, unique=True)

    class Meta:
        verbose_name = "3. Kitob kalit so`zlari"
        verbose_name_plural = "3. Kitoblar kalit so`zlari"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz)
        super(Tag, self).save(*args, **kwargs)


# ================================= GROUPBOOK ================================ #


class CollectionBook(BaseModel):
    STATUS = (
        ("True", "Mavjud"),
        ("False", "Mavjud emas"),
    )

    SPECIAL_STATUS = (
        ("True", "Maqsus toplam"),
        ("False", "Oddiy toplam"),
    )

    title = models.CharField(max_length=200, verbose_name="Toplam nomi")
    description = models.TextField(
        blank=True, null=True, verbose_name="Toplam haqida qisqacha"
    )
    body = RichTextUploadingField(blank=True, null=True, verbose_name="Toplam haqida")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    slug = models.SlugField(max_length=350, null=False, unique=True)
    image = ProcessedImageField(
        upload_to="images/",
        processors=[ResizeToFill(370, 400)],
        format="JPEG",
        options={"quality": 100},
        null=True,
        blank=True,
        verbose_name="Toplam rasmi",
    )
    status = models.CharField(
        max_length=15, choices=STATUS, default="True", verbose_name="Mavjudligi"
    )
    special_status = models.CharField(
        max_length=20,
        choices=SPECIAL_STATUS,
        default="False",
        verbose_name="Sotuv holati",
    )

    class Meta:
        verbose_name = "4. Kitob toplami"
        verbose_name_plural = "4. Kitoblar toplami"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz)
        super(CollectionBook, self).save(*args, **kwargs)


# =================================== BOOK =================================== #


class Book(BaseModel):
    STATUS = (
        ("True", "Mavjud"),
        ("False", "Mavjud emas"),
    )

    SALES_STATUS = (
        ("CHEGIRMA", "CHEGIRMA"),
        ("YANGI", "YANGI"),
        ("FALSE", "Yoq"),
    )
    title = models.CharField(max_length=200, unique=True, verbose_name="Kitob nomi")
    detail = RichTextUploadingField(verbose_name="Kitob haqida")
    coverpage = ProcessedImageField(
        upload_to="books/",
        processors=[ResizeToFill(450, 565)],
        format="JPEG",
        options={"quality": 100},
        verbose_name="Kitobning rasmi",
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Narxi")
    discount_price = models.IntegerField(default=0, verbose_name="Chegirma")
    author = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Muallifi"
    )
    isbn = models.CharField(max_length=500, blank=True, null=True, verbose_name="ISBN")
    language = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Kitob tili"
    )
    date_published = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Kitob shiqgan sana"
    )
    publisher = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Kim tomonidan nashr qilindi",
    )
    category = models.ManyToManyField(
        Category, blank=True, related_name="book", verbose_name="Kitob kategoriyasi"
    )
    tags = models.ManyToManyField(
        Tag, blank=True, related_name="book", verbose_name="Kalit so`zlar"
    )
    collection_book = models.ManyToManyField(
        CollectionBook, blank=True, related_name="book", verbose_name="Kitob toplami"
    )
    wishlist = models.ManyToManyField(User, blank=True, related_name="book")
    status = models.CharField(
        max_length=10, choices=STATUS, default="True", verbose_name="Kitob Mavjudligi"
    )
    sales_status = models.CharField(
        max_length=15,
        choices=SALES_STATUS,
        default="False",
        verbose_name="Sotuvdagi holati",
    )
    slug = models.SlugField(max_length=350, null=False, unique=True)
    rating = models.IntegerField(default=0, verbose_name="Reyting")
    count_comment = models.IntegerField(default=0, verbose_name="Izohlar soni")

    class Meta:
        verbose_name = "1. Kitob"
        verbose_name_plural = "1. Kitoblar"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    @property
    def get_discount_price(self):
        if self.discount_price:
            return self.price - (self.discount_price * (self.price / 100))
        else:
            return self.price

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz)
        super(Book, self).save(*args, **kwargs)


# ================================ BOOK SLIDER =============================== #


class BookSlider(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="bookslider")
    image = ProcessedImageField(
        upload_to="books/",
        processors=[ResizeToFill(450, 565)],
        format="JPEG",
        options={"quality": 100},
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "6. Kitob slider rasmi"
        verbose_name_plural = "6. Kitoblar slider rasmi"

    def __str__(self):
        return self.book.title


# ============================= COLLECTION SLIDER ============================ #


class CollectionSlider(BaseModel):
    collection = models.ForeignKey(
        CollectionBook, on_delete=models.CASCADE, related_name="collectionslider"
    )
    image = ProcessedImageField(
        upload_to="collection/",
        processors=[ResizeToFill(450, 565)],
        format="JPEG",
        options={"quality": 100},
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "6. Collection slider rasmi"
        verbose_name_plural = "6. Collection slider rasmi"

    def __str__(self):
        return self.collection.title


# =============================== BOOK COMMENT =============================== #


class BookComment(BaseModel):
    STATUS = (
        ("True", "Mavjud"),
        ("False", "Mavjud emas"),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="bookcomment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookcomment")
    comment = models.CharField(max_length=255, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default="True")

    class Meta:
        verbose_name = "5. Kitob izohi"
        verbose_name_plural = "5. Kitoblar izohi"

    def __str__(self):
        return self.book.title