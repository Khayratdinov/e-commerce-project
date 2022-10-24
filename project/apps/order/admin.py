from django.contrib import admin

# ============================================================================ #
from project.apps.order.models import Order, OrderLineItem, Shipping

# ======================== REGISTER YOUR MODELS HERE. ======================== #
admin.site.register(Order)
admin.site.register(OrderLineItem)
admin.site.register(Shipping)
