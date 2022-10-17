from django.urls import path

# ============================================================================ #
from project.apps.users import views


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
]
