from atexit import register
from django.contrib import admin

# ============================================================================ #
from project.apps.common.models import (
    HomeSlider,
    CommonInfo,
    HeadImages,
    ContactMessage,
    ShippingInfo,
    PaymentInfo,
    About,
    DiscountInfo,
    FAQ,
)

from modeltranslation.admin import (
    TabbedTranslationAdmin,
    TabbedExternalJqueryTranslationAdmin,
)


class CommonInfoAdmin(TabbedTranslationAdmin):
    pass


class HomeSliderAdmin(TabbedTranslationAdmin):
    list_display = [
        "title",
    ]

    list_per_page = 20


class ShippingInfoAdmin(TabbedTranslationAdmin):
    pass


class PaymentInfoAdmin(TabbedTranslationAdmin):
    pass


class AboutAdmin(TabbedTranslationAdmin):
    pass


class DiscountInfoAdmin(TabbedTranslationAdmin):
    pass


# ======================== REGISTER YOUR MODELS HERE. ======================== #

admin.site.register(HomeSlider, HomeSliderAdmin)
admin.site.register(CommonInfo, CommonInfoAdmin)
admin.site.register(HeadImages)
admin.site.register(ContactMessage)
admin.site.register(FAQ)

admin.site.register(ShippingInfo, ShippingInfoAdmin)
admin.site.register(PaymentInfo, PaymentInfoAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(DiscountInfo, DiscountInfoAdmin)