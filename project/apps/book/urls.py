from django.urls import path

# ============================================================================ #
from project.apps.book import views
from project.apps.book.views import collection_book_list2

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<str:slug>/", views.book_detail, name="book_detail"),
    path(
        "category_detail/<str:slug>/",
        views.book_list_by_category,
        name="category_detail",
    ),
    path("tag_detail/<str:slug>/", views.book_list_by_tag, name="book_list_by_tag"),
    path("add_comment/<int:book_id>", views.add_comment, name="add_comment"),
    path(
        "collection/book_list/",
        collection_book_list2,
        name="collection_book_list",
    ),
    path(
        "collection/<str:slug>/",
        views.collection_book_detail,
        name="collection_book_detail",
    ),
]