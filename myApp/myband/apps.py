from django.apps import AppConfig


class MybandConfig(AppConfig):
    """
    AppConfig class for the 'myband' app.

    Inherits from Django's AppConfig and provides configuration for the 'myband' app.

    Attributes:
        - default_auto_field: The default auto-generated field for models.
        - name: The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myband'
