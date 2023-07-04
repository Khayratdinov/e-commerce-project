import os
from pathlib import Path
import environ


from django.utils.translation import gettext_lazy as _

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
PROJECT_DIR = ROOT_DIR / "project"
BASE_DIR = ROOT_DIR
environ.Env.read_env(os.path.join(ROOT_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost"]


# CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:8080",
# ]
# CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://localhost:8000",
]


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",

]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True


# ========================== APPLICATION DEFINITION ========================== #


DJANGO_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    "ckeditor",
    "ckeditor_uploader",
    "imagekit",
    "clickuz",
    "rest_framework",
    "rosetta",
    "corsheaders",
    "payme",
    "paycomuz",
]

LOCAL_APPS = [
    "project.apps.administration",
    "project.apps.core",
    "project.apps.common",
    "project.apps.book",
    "project.apps.users",
    "project.apps.order",
    "project.apps.blog",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "project.apps.cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# ============================ PASSWORD VALIDATION =========================== #

# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =========================== INTERNATIONALIZATION =========================== #

# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "uz"

LANGUAGES = [
    ("uz", _("Uzbek")),
    ("en", _("English")),
    ("ru", _("Russian")),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"
MODELTRANSLATION_PREPOPULATE_LANGUAGE = "uz"

# time zone UTC + 5 for models created_at i need + 5 hour

TIME_ZONE = "Asia/Tashkent"


USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(ROOT_DIR, "locale"),
]


# =============================== STATIC FILES =============================== #
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"

STATICFILES_DIRS = [str(PROJECT_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


MEDIA_ROOT = str(ROOT_DIR / "mediafiles")
MEDIA_URL = "/media/"


CKEDITOR_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"

CKEDITOR_UPLOAD_PATH = "images/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono",
        # 'skin': 'office2013',
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "document",
                "items": [
                    "Source",
                    "-",
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "-",
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "Link",
                    "Unlink",
                    "-",
                    "Image",
                    "Table",
                    "HorizontalRule",
                    "-",
                    "Preview",
                    "Maximize",
                ],
            },
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        "height": 291,
        "width": "100%",
        "filebrowserWindowHeight": 725,
        "filebrowserWindowWidth": 940,
        "toolbarCanCollapse": True,
        # "mathJaxLib": "//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML",
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                # your extra plugins here
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ]
        ),
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"


LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

CART_SESSION_ID = "cart"


CLICK_SETTINGS = {
    "service_id": env("SERVICE_ID"),
    "merchant_id": env("SERVICE_ID"),
    "secret_key": env("SECRET_KEY_CLICK"),
    "merchant_user_id": env("MERCHANT_USER_ID"),
}


PAYCOM_SETTINGS = {
    "KASSA_ID": env("PAYME_ID"),  # token
    "SECRET_KEY": env("PAYME_KEY"),  # password
    "TOKEN": env("TOKEN"),
    "ACCOUNTS": {"KEY": "order_id"},
}