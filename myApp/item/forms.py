from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    """
    Form for creating a new item.

    Fields:
        - category: The category of the item.
        - artist: The artist of the item.
        - description: The description of the item.
        - genre: The genre of the item.
        - image: The image of the item.

    """
    class Meta: 
        model = Item
        fields = ('category', 'artist', 'description', 'genre', 'image',)
        widgets = {
            'categroy': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

            'artist': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

            'genre': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }