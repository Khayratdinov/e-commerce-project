from django.urls import path

# ============================================================================ #
from project.apps.order import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("create/", views.order_create, name="order_create"),
    path("detail/", views.order_detail, name="order_detail"),
]
