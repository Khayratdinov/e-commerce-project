from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [] + i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
    path("", include("project.apps.common.urls")),
    path("books/", include("project.apps.book.urls")),
    path("auth/", include("project.apps.users.urls")),
    path("cart/", include("project.apps.cart.urls")),
    path("order/", include("project.apps.order.urls")),
    path("blog/", include("project.apps.blog.urls")),
    path("administration/", include("project.apps.administration.urls")),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
