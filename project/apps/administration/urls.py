from django.urls import path

# ============================================================================ #
from project.apps.administration import views

urlpatterns = [
    path("", views.index, name="dashboard"),
]
