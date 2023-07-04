from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project.apps.order"
    verbose_name = "2. Buyirtmalarga bogliq dasturlar"
    ordering = 2