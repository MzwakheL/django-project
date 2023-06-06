from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
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