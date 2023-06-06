from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Item

from item.models import Item


# Create your views here.

@login_required

def index(request):
    items = Item.objects.all()  # Change 'Item.Objects.all()' to 'Item.objects.all()'
    return render(request, 'dashboard/index.html', {
        'items': items
    })