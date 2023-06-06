from django.db import models

# Create your models here.

class Item(models.Model):
    # Define your Item model fields here
    name = models.CharField(max_length=100)
    # Other fields...

    def __str__(self):
        return self.name
