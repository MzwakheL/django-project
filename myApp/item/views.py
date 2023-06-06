from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import NewItemForm
from .models import Category, Item


# Create your views here.

def items(request):
    """
    View function for displaying items.

    The view displays a list of items based on optional query parameters.

    Query parameters:
        - query: A search query string.
        - category: The ID of a category to filter the items.

    """
    query = request.GET.get('query,' '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter()

    if category_id: 
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query)) | Q(description__incontains=query)

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def detail(request, pk): 
    """
    View function for displaying item details.

    Args:
        - pk: The primary key of the item.

    """
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'items/detail.html', {
        'item': item
    })


@login_required
def new(request):
    """
    View function for creating a new item.

    The view handles a form to create a new item and save it to the database.

    """
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def delete(request, pk):
    """
    View function for deleting an item.

    Args:
        - pk: The primary key of the item.

    """
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')