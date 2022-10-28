from django.urls import path

# ============================================================================ #
from project.apps.administration import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    # ================================= CATEGORY ================================= #
    path("category_admin/", views.category_admin, name="category_admin"),
    path("category_create/", views.category_create, name="category_create"),
    path("category_edit/<int:pk>/", views.category_edit, name="category_edit"),
    path("category_delete/<int:pk>/", views.category_delete, name="category_delete"),
    # =================================== BOOK =================================== #
    path("book_admin/", views.book_admin, name="book_admin"),
    path("book_create/", views.book_create, name="book_create"),
    path("book_edit/<int:pk>/", views.book_edit, name="book_edit"),
    path("book_delete/<int:pk>/", views.book_delete, name="book_delete"),
]
