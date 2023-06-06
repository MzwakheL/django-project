from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Item

from item.models import Item


# Create your views here.

@login_required

def index(request):
    """
    View function for the dashboard index page.

    Retrieves all items from the Item model and renders them on the index page.

    Parameters:
        - request: The HTTP request object.

    Returns:
        The rendered HTML template response with the retrieved items.
    """
    items = Item.objects.all()  # Change 'Item.Objects.all()' to 'Item.objects.all()'
    return render(request, 'dashboard/index.html', {
        'items': items
    })