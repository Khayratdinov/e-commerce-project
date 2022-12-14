import os
from pathlib import Path
import environ
import os

from django.utils.translation import gettext_lazy as _

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
PROJECT_DIR = ROOT_DIR / "project"
environ.Env.read_env(os.path.join(ROOT_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["*"]


# ========================== APPLICATION DEFINITION ========================== #


DJANGO_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "ckeditor",
    "ckeditor_uploader",
    "imagekit",
    "debug_toolbar",
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
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
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
    ("en", _("English")),
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"
MODELTRANSLATION_PREPOPULATE_LANGUAGE = "uz"

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


MEDIA_ROOT = str(PROJECT_DIR / "media")
MEDIA_URL = "/media/"


CKEDITOR_JQUERY_URL = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"

CKEDITOR_UPLOAD_PATH = "images/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 200,
        "width": 750,
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CART_SESSION_ID = "cart"
