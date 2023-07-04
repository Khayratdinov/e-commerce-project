from .base import *


ALLOWED_HOSTS = ["*"]


INSTALLED_APPS += [
    "debug_toolbar",
]


INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE.insert(
    0,
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)


# ================================= DATABASE ================================= #

# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ROOT_DIR / "db.sqlite3",
    }
}


MEDIA_ROOT = str(PROJECT_DIR / "media")
MEDIA_URL = "/media/"


# def show_toolbar(request):
#     return True


# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK": show_toolbar,
# }

# if DEBUG:
#     import mimetypes

#     mimetypes.add_type("application/javascript", ".js", True)