# Generated by Django 4.2.2 on 2023-07-04 15:59

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Kitob nomi"
                    ),
                ),
                (
                    "title_uz",
                    models.CharField(
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name="Kitob nomi",
                    ),
                ),
                (
                    "title_en",
                    models.CharField(
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name="Kitob nomi",
                    ),
                ),
                (
                    "title_ru",
                    models.CharField(
                        max_length=200,
                        null=True,
                        unique=True,
                        verbose_name="Kitob nomi",
                    ),
                ),
                (
                    "detail",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="Kitob haqida"
                    ),
                ),
                (
                    "detail_uz",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        null=True, verbose_name="Kitob haqida"
                    ),
                ),
                (
                    "detail_en",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        null=True, verbose_name="Kitob haqida"
                    ),
                ),
                (
                    "detail_ru",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        null=True, verbose_name="Kitob haqida"
                    ),
                ),
                (
                    "coverpage",
                    imagekit.models.fields.ProcessedImageField(
                        upload_to="books/", verbose_name="Kitobning rasmi"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Narxi"
                    ),
                ),
                (
                    "discount_price",
                    models.IntegerField(default=0, verbose_name="Chegirma"),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Muallifi"
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="ISBN"
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Kitob tili"
                    ),
                ),
                (
                    "date_published",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Kitob shiqgan sana",
                    ),
                ),
                (
                    "publisher",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Kim tomonidan nashr qilindi",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "Mavjud"), ("False", "Mavjud emas")],
                        default="True",
                        max_length=10,
                        verbose_name="Kitob Mavjudligi",
                    ),
                ),
                (
                    "sales_status",
                    models.CharField(
                        choices=[
                            ("CHEGIRMA", "CHEGIRMA"),
                            ("YANGI", "YANGI"),
                            ("FALSE", "Yoq"),
                        ],
                        default="False",
                        max_length=15,
                        verbose_name="Sotuvdagi holati",
                    ),
                ),
                ("slug", models.SlugField(max_length=350, unique=True)),
                ("rating", models.IntegerField(default=0, verbose_name="Reyting")),
                (
                    "count_comment",
                    models.IntegerField(default=0, verbose_name="Izohlar soni"),
                ),
            ],
            options={
                "verbose_name": "1. Kitob",
                "verbose_name_plural": "1. Kitoblar",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="Kategoriya nomi"),
                ),
                (
                    "title_uz",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Kategoriya nomi"
                    ),
                ),
                (
                    "title_en",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Kategoriya nomi"
                    ),
                ),
                (
                    "title_ru",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Kategoriya nomi"
                    ),
                ),
                ("slug", models.SlugField(max_length=350, unique=True)),
            ],
            options={
                "verbose_name": "2. Kitob kategoriyasi",
                "verbose_name_plural": "2. Kitoblar kategoriyasi",
            },
        ),
        migrations.CreateModel(
            name="CollectionBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=200, verbose_name="Toplam nomi")),
                (
                    "title_uz",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Toplam nomi"
                    ),
                ),
                (
                    "title_en",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Toplam nomi"
                    ),
                ),
                (
                    "title_ru",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Toplam nomi"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Toplam haqida qisqacha"
                    ),
                ),
                (
                    "description_uz",
                    models.TextField(
                        blank=True, null=True, verbose_name="Toplam haqida qisqacha"
                    ),
                ),
                (
                    "description_en",
                    models.TextField(
                        blank=True, null=True, verbose_name="Toplam haqida qisqacha"
                    ),
                ),
                (
                    "description_ru",
                    models.TextField(
                        blank=True, null=True, verbose_name="Toplam haqida qisqacha"
                    ),
                ),
                (
                    "body",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Toplam haqida"
                    ),
                ),
                (
                    "body_uz",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Toplam haqida"
                    ),
                ),
                (
                    "body_en",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Toplam haqida"
                    ),
                ),
                (
                    "body_ru",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Toplam haqida"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Narxi"
                    ),
                ),
                ("slug", models.SlugField(max_length=350, unique=True)),
                (
                    "image",
                    imagekit.models.fields.ProcessedImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="Toplam rasmi",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "Mavjud"), ("False", "Mavjud emas")],
                        default="True",
                        max_length=15,
                        verbose_name="Mavjudligi",
                    ),
                ),
                (
                    "special_status",
                    models.CharField(
                        choices=[("True", "Maqsus toplam"), ("False", "Oddiy toplam")],
                        default="False",
                        max_length=20,
                        verbose_name="Sotuv holati",
                    ),
                ),
            ],
            options={
                "verbose_name": "4. Kitob toplami",
                "verbose_name_plural": "4. Kitoblar toplami",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="Kalit so`z nomi"),
                ),
                (
                    "title_uz",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Kalit so`z nomi"
                    ),
                ),
                (
                    "title_en",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Kalit so`z nomi"
                    ),
                ),
                (
                    "title_ru",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Kalit so`z nomi"
                    ),
                ),
                ("slug", models.SlugField(max_length=350, unique=True)),
            ],
            options={
                "verbose_name": "3. Kitob kalit so`zlari",
                "verbose_name_plural": "3. Kitoblar kalit so`zlari",
            },
        ),
        migrations.CreateModel(
            name="CollectionSlider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    imagekit.models.fields.ProcessedImageField(
                        blank=True, null=True, upload_to="collection/"
                    ),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="collectionslider",
                        to="book.collectionbook",
                    ),
                ),
            ],
            options={
                "verbose_name": "6. Collection slider rasmi",
                "verbose_name_plural": "6. Collection slider rasmi",
            },
        ),
        migrations.CreateModel(
            name="BookSlider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    imagekit.models.fields.ProcessedImageField(
                        blank=True, null=True, upload_to="books/"
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookslider",
                        to="book.book",
                    ),
                ),
            ],
            options={
                "verbose_name": "6. Kitob slider rasmi",
                "verbose_name_plural": "6. Kitoblar slider rasmi",
            },
        ),
        migrations.CreateModel(
            name="BookComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("comment", models.CharField(blank=True, max_length=255)),
                ("rate", models.IntegerField(default=1)),
                ("ip", models.CharField(blank=True, max_length=20)),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "Mavjud"), ("False", "Mavjud emas")],
                        default="True",
                        max_length=10,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookcomment",
                        to="book.book",
                    ),
                ),
            ],
            options={
                "verbose_name": "5. Kitob izohi",
                "verbose_name_plural": "5. Kitoblar izohi",
            },
        ),
    ]
