from django.contrib import messages
from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter()
    categories = Category.objects.all()

    return render(request, 'band/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'band/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
             # Redirect to the login page
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect ('myband:login')
        else:
            messages.error(request, 'There was an error creating your account.')

    else:
        form = SignupForm()

    return render(request, 'band/signup.html', {
        'form': form
    })