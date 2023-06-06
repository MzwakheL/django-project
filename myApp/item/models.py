from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

# Set string representation for the class
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='Album', on_delete=models.CASCADE)
    artist = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='album_images', blank=True, null=True)

    def __str__(self):
        return self.artist
