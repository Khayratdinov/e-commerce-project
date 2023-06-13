from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project.apps.book"
    verbose_name = "1. Kitobga bogliq dasturlar"
    ordering = 1