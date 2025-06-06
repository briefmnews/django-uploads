SECRET_KEY = "dump-secret-key"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "uploads",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

UPLOADS_WARNING_SIZE = 307200  # 300KB