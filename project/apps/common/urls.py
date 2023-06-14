from django.urls import path

# ============================================================================ #
from project.apps.common import views


urlpatterns = [
    path("", views.index, name="home"),
    path("contact_message/", views.contact_message, name="contact_message"),
    path("search/", views.search, name="search"),

    path("shipping_info/", views.shipping_info, name="shipping_info"),
    path("payment_info/", views.payment_info, name="payment_info"),
    path("discount_info/", views.discount_info, name="discount_info"),
    path("about_info/", views.about_info, name="about_info"),
]