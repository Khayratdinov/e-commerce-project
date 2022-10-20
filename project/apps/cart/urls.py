from django.urls import path

# ============================================================================ #
from . import views

urlpatterns = [
    # =================================== CART =================================== #
    path("cart_detail/", views.cart_detail, name="cart_detail"),
    path("cart_add/<int:book_id>/", views.cart_add, name="cart_add"),
    path("cart_remove/<int:book_id>/", views.cart_remove, name="cart_remove"),
    path("cart-update/", views.cart_update, name="cart_update"),
]
