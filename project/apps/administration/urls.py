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
    # =================================== TAG =================================== #
    path("tag_admin/", views.tag_book_admin, name="tag_admin"),
    path("tag_create/", views.tag_book_create, name="tag_create"),
    path("tag_edit/<int:pk>/", views.tag_book_edit, name="tag_edit"),
    path("tag_delete/<int:pk>/", views.tag_book_delete, name="tag_delete"),
    # =============================== BOOK COMMENT =============================== #
    path("book_comment_admin/", views.book_comment_admin, name="book_comment_admin"),
    path(
        "book_comment_detail/<int:pk>/",
        views.book_comment_detail,
        name="book_comment_detail",
    ),
    path(
        "book_comment_edit/<int:pk>/", views.book_comment_edit, name="book_comment_edit"
    ),
    path(
        "book_comment_delete/<int:pk>/",
        views.book_comment_delete,
        name="book_comment_delete",
    ),
    # ================================ HOME SLIDER =============================== #
    path("home_slider_admin/", views.home_slider_admin, name="home_slider_admin"),
    path("home_slider_create/", views.home_slider_create, name="home_slider_create"),
    path("home_slider_edit/<int:pk>/", views.home_slider_edit, name="home_slider_edit"),
    path(
        "home_slider_delete/<int:pk>/",
        views.home_slider_delete,
        name="home_slider_delete",
    ),
]
