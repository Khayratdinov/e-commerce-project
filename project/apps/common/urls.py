from django.urls import path

# ============================================================================ #
from project.apps.common import views


urlpatterns = [path("", views.index, name="home")]
