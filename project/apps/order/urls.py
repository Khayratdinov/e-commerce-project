from django.urls import path

# ============================================================================ #
from project.apps.order import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path(
        "collection/checkout/<int:collection_id>/",
        views.collection_checkout,
        name="collection_checkout",
    ),
    path("create/", views.order_create, name="order_create"),
    path("detail/<int:code>/", views.order_detail, name="order_detail"),
    path(
        "successfully_payment_order_cash/<int:code>/",
        views.successfully_payment_order_cash,
        name="successfully_payment_order_cash",
    ),
    
]