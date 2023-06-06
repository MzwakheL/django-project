from django.db import models

# Create your models here.

class Item(models.Model):
    """
    Model representing an item.

    Fields:
        - name: The name of the item (max length: 100 characters).

    Methods:
        - __str__: Returns a string representation of the item (name).

    """
    # Define your Item model fields here
    name = models.CharField(max_length=100)
    # Other fields...

    def __str__(self):
        """
        Returns a string representation of the item.

        Returns:
            A string containing the name of the item.
        """
        return self.name
