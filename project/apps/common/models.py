from unittest.mock import Base
from django.db import models

# ============================================================================ #
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# ============================================================================ #


# ================================ BASE MODEL ================================ #


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ======================== COMMON INFORMATION WEBSITE ======================== #


class CommonInfo(BaseModel):

    STATUS = (
        ("True", "True"),
        ("False", "False"),
    )

    logo = models.ImageField(blank=True, upload_to="images/")

    description_contact = models.TextField(blank=True)
    description_footer = models.TextField(blank=True)

    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default="False")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


# ================================ HOMESLIDER ================================ #


class HomeSlider(BaseModel):

    STATUS = (
        ("True", "Published"),
        ("False", "Not Published"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    shape = models.ImageField(blank=True, upload_to="images/")
    cover = models.ImageField(blank=True, upload_to="images/")
    status = models.CharField(max_length=15, choices=STATUS, default="True")
    url = models.CharField(max_length=555, blank=True)

    def __str__(self):
        return self.title


# =============================== HEADER IMAGES ============================== #


class HeadImages(BaseModel):

    STATUS = (
        ("True", "Available"),
        ("False", "Not Available"),
    )

    image = ProcessedImageField(
        upload_to="images/",
        processors=[ResizeToFill(1920, 1285)],
        format="JPEG",
        options={"quality": 100},
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=15, choices=STATUS, default="True")


# ============================== CONTACTMESSAGE ============================== #


class ContactMessage(models.Model):

    STATUS = (
        ("True", "Oqilgan"),
        ("False", "Oqilmagan"),
    )

    name = models.CharField(max_length=222)
    phone = models.CharField(max_length=222)
    subject = models.CharField(blank=True, max_length=255)
    message = models.TextField(max_length=500)
    ip = models.CharField(max_length=155, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default="False")
    create_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return self.name
