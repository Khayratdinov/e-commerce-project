from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(blank=True, null=True, max_length=20, unique=True)
    street_address_1 = models.CharField(blank=True, max_length=150)
    street_address_2 = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=80)
    bio = models.TextField(max_length=400, blank=True)
    instagram_link = models.CharField(max_length=200, blank=True, null=True)
    telegram_link = models.CharField(max_length=200, blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "1. Foydalanuvchi"
        verbose_name_plural = "1. Foydalanuvchilar"