from django.urls import path

# ============================================================================ #

from project.apps.administration import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("general_dashboard/", views.general_dashboard, name="general_dashboard"),
    path("weekly_dashboard/", views.weekly_dashboard, name="weekly_dashboard"),
    path("monthly_dashboard/", views.monthly_dashboard, name="monthly_dashboard"),
    path('yearly_dashboard/', views.yearly_dashboard, name='yearly_dashboard'),
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
    path("order_dashboard/", views.order_dashboard, name="order_dashboard"),
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
    # =============================== CATEGORY BLOG ============================== #
    path("category_blog_admin/", views.category_blog_admin, name="category_blog_admin"),
    path(
        "category_blog_create/", views.category_blog_create, name="category_blog_create"
    ),
    path(
        "category_blog_edit/<int:pk>/",
        views.category_blog_edit,
        name="category_blog_edit",
    ),
    path(
        "category_blog_delete/<int:pk>/",
        views.category_blog_delete,
        name="category_blog_delete",
    ),
    # =================================== BLOG =================================== #
    path("blog_admin/", views.blog_admin, name="blog_admin"),
    path("blog_create/", views.blog_create, name="blog_create"),
    path("blog_edit/<int:pk>/", views.blog_edit, name="blog_edit"),
    path("blog_delete/<int:pk>/", views.blog_delete, name="blog_delete"),
    # =============================== RANDOM IMAGES ============================== #
    path("random_image_admin/", views.random_image_admin, name="random_image_admin"),
    path("random_image_create/", views.random_image_create, name="random_image_create"),
    path(
        "random_image_edit/<int:pk>/", views.random_image_edit, name="random_image_edit"
    ),
    path(
        "random_image_delete/<int:pk>/",
        views.random_image_delete,
        name="random_image_delete",
    ),
    # =============================== SETTING SITE =============================== #
    path("setting_site_admin/", views.setting_site_admin, name="setting_site_admin"),
    path("setting_site_create/", views.setting_site_create, name="setting_site_create"),
    path(
        "setting_site_edit/<int:pk>/", views.setting_site_edit, name="setting_site_edit"
    ),
    path(
        "setting_site_delete/<int:pk>/",
        views.setting_site_delete,
        name="setting_site_delete",
    ),
    # ============================== CONTACT MESSAGE ============================= #
    path(
        "contact_message_admin/",
        views.contact_message_admin,
        name="contact_message_admin",
    ),
    path(
        "contact_message_detail/<int:pk>/",
        views.contact_message_detail,
        name="contact_message_detail",
    ),
    path(
        "contact_message_delete/<int:pk>/",
        views.contact_message_delete,
        name="contact_message_delete",
    ),

     # ============================= COLLECTION BOOKS ============================= #


    path('collection_admin/', views.collection_book_admin, name='collection_book_admin'),
    path('collection_create/', views.collection_book_create, name='collection_create'),
    path('collection_edit/<int:pk>/', views.collection_edit, name='collection_edit'),
    path('collection_delete/<int:pk>/', views.collection_delete, name='collection_delete'),
]
