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
    # =================================== ORDER ================================== #
    path("order_list/", views.order_list, name="order_list"),
    path("order_detail/<int:id>/", views.order_detail, name="order_detail"),
    # ================================= SHIPPING ================================= #
    path("shipping_admin/", views.shipping_admin, name="shipping_admin"),
    path("shipping_create/", views.shipping_create, name="shipping_create"),
    path("shipping_edit/<int:pk>/", views.shipping_edit, name="shipping_edit"),
    path("shipping_delete/<int:pk>/", views.shipping_delete, name="shipping_delete"),
    # =================================== USER =================================== #
    path("user_admin/", views.user_admin, name="user_admin"),
    path("user_detail/<int:pk>/", views.user_detail, name="user_detail"),
    path("user_edit/<int:pk>/", views.user_edit, name="user_edit"),
    path("user_delete/<int:pk>/", views.user_delete, name="user_delete"),
    # ================================= SHOP CART ================================ #
    path(
        "add_to_shopcart_admin/<str:slug>/",
        views.add_to_shopcart,
        name="add_to_shopcart_admin",
    ),
    path(
        "delete_from_cart_admin/<int:id>/",
        views.delete_from_cart,
        name="delete_from_cart_admin",
    ),
    path("shopcart_admin/", views.shopcart, name="shopcart_admin"),
]
