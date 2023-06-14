from django.db import models

# ============================================================================ #
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

# ============================================================================ #


# ================================ BASE MODEL ================================ #
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ========================== BASE MODEL WITH STATUS ========================== #


class BaseModelWithStatus(models.Model):
    STATUS = (
        ("True", "Mavjud"),
        ("False", "Mavjud emas"),
    )

    status = models.CharField(max_length=15, choices=STATUS, default="False")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ======================== COMMON INFORMATION WEBSITE ======================== #


class CommonInfo(BaseModelWithStatus):
    logo = models.ImageField(upload_to="images/", blank=True, null=True)

    description_contact = models.TextField(blank=True, null=True)
    description_footer = models.TextField(blank=True, null=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    telegram = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "1. Saytning umimiy malumoti"
        verbose_name_plural = "1. Saytning umimiy malumoti"


# ================================ HOMESLIDER ================================ #


class HomeSlider(BaseModelWithStatus):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cover = ProcessedImageField(
        upload_to="images/",
        processors=[ResizeToFill(1920, 748)],
        format="JPEG",
        options={"quality": 100},
        null=True,
        blank=True,
    )
    url = models.CharField(max_length=555, blank=True, null=True)

    class Meta:
        verbose_name = "2. Bosh sahifa ushin rasim"
        verbose_name_plural = "2. Bosh sahifa ushin rasim"

    def __str__(self):
        return self.title


# =============================== HEADER IMAGES ============================== #


class HeadImages(BaseModelWithStatus):
    image = ProcessedImageField(
        upload_to="images/",
        processors=[ResizeToFill(1920, 1285)],
        format="JPEG",
        options={"quality": 100},
    )

    class Meta:
        verbose_name = "3. Sahifalarda shiqadigan rasm (Head Image)"
        verbose_name_plural = "3. Sahifalarda shiqadigan rasm (Head Image)"


# ============================== CONTACTMESSAGE ============================== #


class ContactMessage(BaseModel):
    STATUS = (
        ("True", "Oqilgan"),
        ("False", "Oqilmagan"),
    )

    name = models.CharField(max_length=222)
    phone = models.CharField(max_length=222)
    subject = models.CharField(blank=True, max_length=255)
    message = models.TextField(max_length=500)
    ip = models.CharField(max_length=155, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default="False")
    read = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "4. Bizga kelgan xabar"
        verbose_name_plural = "4. Bizga kelgan xabarlar"

    def __str__(self):
        return self.name


class FAQ(BaseModelWithStatus):
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "5. Ko`p beriladigan savol"
        verbose_name_plural = "5. Ko`p beriladigan savollar"


class About(BaseModelWithStatus):
    detail = RichTextUploadingField()

    class Meta:
        verbose_name = "6. Biz haqqimizda malumot"
        verbose_name_plural = "6. Biz haqqimizda malumot"


class ShippingInfo(BaseModelWithStatus):
    detail = RichTextUploadingField()

    class Meta:
        verbose_name = "7. Yetkazip berish haqqida"
        verbose_name_plural = "7. Yetkazip berish haqqida"


class PaymentInfo(BaseModelWithStatus):
    detail = RichTextUploadingField()

    class Meta:
        verbose_name = "8. Tolov tizimi haqqida"
        verbose_name_plural = "8. Tolov tizimi haqqida"


class DiscountInfo(BaseModelWithStatus):
    detail = RichTextUploadingField()

    class Meta:
        verbose_name = "9. Chegirmalar haqqida"
        verbose_name_plural = "9. Chegirmalar haqqida"