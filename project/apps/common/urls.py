from django.urls import path

# ============================================================================ #
from project.apps.common import views


urlpatterns = [
    path("", views.index, name="home"),
    path("contact_message/", views.contact_message, name="contact_message"),
    path('search/', views.search, name='search'),
]
