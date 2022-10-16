from atexit import register
from django.contrib import admin

# ============================================================================ #
from project.apps.common.models import HomeSlider

# Register your models here.


# ================================= REGISTER ================================= #

admin.site.register(HomeSlider)
