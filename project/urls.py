from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("project.apps.common.urls")),
    path("books/", include("project.apps.book.urls")),
    path("auth/", include("project.apps.users.urls")),
    path("cart/", include("project.apps.cart.urls")),
    path("order/", include("project.apps.order.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
