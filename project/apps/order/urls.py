from django.urls import path

# ============================================================================ #
from project.apps.order import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
]
