# Generated by Django 4.1.2 on 2022-11-28 07:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=355)),
                ("title_en", models.CharField(max_length=355, null=True)),
                ("title_ru", models.CharField(max_length=355, null=True)),
                ("title_uz", models.CharField(max_length=355, null=True)),
                (
                    "image",
                    imagekit.models.fields.ProcessedImageField(upload_to="blog/"),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                ("description_ru", models.TextField(blank=True, null=True)),
                ("description_uz", models.TextField(blank=True, null=True)),
                ("text", ckeditor_uploader.fields.RichTextUploadingField()),
                ("text_en", ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ("text_ru", ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ("text_uz", ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "Published"), ("False", "Not Published")],
                        default="True",
                        max_length=15,
                    ),
                ),
                ("views", models.PositiveBigIntegerField(default=0)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CategoryBlog",
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
                ("title", models.CharField(max_length=50)),
                ("title_en", models.CharField(max_length=50, null=True)),
                ("title_ru", models.CharField(max_length=50, null=True)),
                ("title_uz", models.CharField(max_length=50, null=True)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BlogComment",
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
                ("name", models.CharField(max_length=55)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("comment", models.TextField(max_length=355)),
                ("ip", models.CharField(blank=True, max_length=20)),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "No Block"), ("False", "Block")],
                        default="True",
                        max_length=15,
                    ),
                ),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blog"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.categoryblog"
            ),
        ),
    ]
