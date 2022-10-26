from django.urls import path

# ============================================================================ #
from project.apps.blog import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<slug:slug>/", views.blog_detail, name="blog_detail"),
    path(
        "category_blog_detail/<slug:slug>/",
        views.category_blog_detail,
        name="category_blog_detail",
    ),
    path(
        "add_comment_to_blog/<int:blog_id>/",
        views.add_comment_to_blog,
        name="add_comment_to_blog",
    ),
]
