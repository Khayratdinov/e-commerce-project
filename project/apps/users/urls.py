from django.urls import path

# ============================================================================ #
from project.apps.users import views


urlpatterns = [
    path("register/", views.signup, name="register"),
    path("login/", views.login_view, name="login"),
    # ============================================================================ #
    path("profile/", views.view_profile, name="view_profile"),
    path(
        "order-detail-user/<int:order>/",
        views.order_detail_user,
        name="order_detail_user",
    ),
    path("wishlist/add/<int:id>/", views.add_wishlist, name="addwishlist"),
    path("wishlist/delete/<int:id>/", views.remove_wishlist, name="remove_wishlist"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("logout/", views.mylogout, name="logout"),
]