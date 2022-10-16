from django.urls import path

# ============================================================================ #
from project.apps.book import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
]
