from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project.apps.common"
    verbose_name = "4. Saytning umimiy malumotlari"
    ordering = 4