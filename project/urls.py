from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from project.apps.order.views import (
    ClickUzView,
    PaymeUzView,
    successfully_payment_payme,
)


urlpatterns = [
    path("click/transaction/", ClickUzView.as_view()),
    path("paycom/", PaymeUzView.as_view()),
    path(
        "successfully_payment_payme/",
        successfully_payment_payme,
        name="successfully_payment_payme",
    ),
] + i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("admin_django_secret/", admin.site.urls),
    path("", include("project.apps.common.urls")),
    path("books/", include("project.apps.book.urls")),
    path("auth/", include("project.apps.users.urls")),
    path("cart/", include("project.apps.cart.urls")),
    path("order/", include("project.apps.order.urls")),
    path("blog/", include("project.apps.blog.urls")),
    path("admin/", include("project.apps.administration.urls")),
    prefix_default_language=False,
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # import debug_toolbar

    # urlpatterns = [
    #     path("__debug__/", include(debug_toolbar.urls)),
    # ] + urlpatterns


if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(
            r"^tarjima-qilish-paneli/",
            include("rosetta.urls"),
        )
    ]


admin.site.site_title = "BookStore Website"
admin.site.site_header = "BookStore Website 2"
admin.site.index_title = "BookStore admin panel"

admin.site.site_header = "Barcha malumotlarni boshqarish bolimi"