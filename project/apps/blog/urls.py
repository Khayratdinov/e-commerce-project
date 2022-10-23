from django.urls import path

# ============================================================================ #
from project.apps.blog import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<slug:slug>/", views.blog_detail, name="blog_detail"),
]
