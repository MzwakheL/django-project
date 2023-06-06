from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """
    AppConfig class for the dashboard app.

    Attributes:
        - default_auto_field: The default auto field for the app's models.
        - name: The name of the app.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
