from django.apps import AppConfig

BLOG_APP_NAME = "app.blog"


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = BLOG_APP_NAME
