from atexit import register
from django.contrib import admin

# ============================================================================ #
from project.apps.common.models import HomeSlider, CommonInfo


# ======================== REGISTER YOUR MODELS HERE. ======================== #

admin.site.register(HomeSlider)
admin.site.register(CommonInfo)
