from slugify import slugify

# ============================================================================ #

from django.db import models
from django.urls import reverse

# ============================================================================ #
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# ============================================================================ #
from project.apps.common.models import BaseModel

# ============================================================================ #
#                                     BLOG                                     #
# ============================================================================ #


class Blog(BaseModel):
    STATUS = (
        ("True", "Chop etilgan"),
        ("False", "Chop etilmagan"),
    )

    title = models.CharField(max_length=355, unique=True)

    description = models.TextField(blank=True, null=True)
    text = RichTextUploadingField()
    image = ProcessedImageField(
        upload_to="blog/",
        processors=[ResizeToFill(1170, 788)],
        format="JPEG",
        options={"quality": 100},
    )
    status = models.CharField(max_length=15, choices=STATUS, default="True")
    category = models.ForeignKey(
        "CategoryBlog", on_delete=models.CASCADE, related_name="blog"
    )
    views = models.PositiveBigIntegerField(default=0)
    slug = models.SlugField(max_length=400, null=False, unique=True)

    class Meta:
        verbose_name = "1. Yangilik"
        verbose_name_plural = "1. Yangiliklar"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz)[:80]
        super(Blog, self).save(*args, **kwargs)


# ============================================================================ #


class CategoryBlog(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, null=False, unique=True)

    class Meta:
        verbose_name = "2. Yangilik kategoryasi"
        verbose_name_plural = "2. Yangiliklar kategoryasi"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_blog_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz)[:50]
        super(CategoryBlog, self).save(*args, **kwargs)


# ============================================================================ #


class BlogComment(BaseModel):
    STATUS = (
        ("True", "Blok qoyilmagan"),
        ("False", "Bloklangan"),
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blogcomment")
    name = models.CharField(max_length=55, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField(max_length=355, blank=False)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default="True")

    class Meta:
        verbose_name = "3. Yangilik izohi"
        verbose_name_plural = "3. Yangiliklar izohi"

    def __str__(self):
        return self.name