from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "resources"
    verbose_name = (
        "المساقات، التخصصات والكليات"  # the name that will appear in the admin panel
    )
