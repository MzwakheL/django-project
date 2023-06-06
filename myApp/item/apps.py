from django.apps import AppConfig


class ItemConfig(AppConfig):
    """
    Configuration class for the 'item' app.

    Attributes:
        default_auto_field (str): The default auto-generated field type.
        name (str): The name of the app.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'item'
