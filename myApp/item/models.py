from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Model representing a category for items.

    Fields:
        - name: The name of the category.

    """
    name = models.CharField(max_length=255)

# Set string representation for the class
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    """
    Model representing an item.

    Fields:
        - category: The category of the item.
        - artist: The artist of the item.
        - description: The description of the item.
        - genre: The genre of the item.
        - image: The image of the item.

    """
    category = models.ForeignKey(Category, related_name='Album', on_delete=models.CASCADE)
    artist = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='album_images', blank=True, null=True)

    def __str__(self):
        return self.artist
