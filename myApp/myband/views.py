from django.contrib import messages
from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm

# Create your views here.

def index(request):
    """
    Render the index page with a list of items and categories.

    Retrieves all items and categories from the database and passes them to the template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """

    items = Item.objects.filter()
    categories = Category.objects.all()

    return render(request, 'band/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    """
    Render the contact page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    return render(request, 'band/contact.html')

def signup(request):
    """
    Render the signup page and handle the signup form submission.

    If the request method is POST, validate the form data and create a new user account.
    If the form is valid, save the form and redirect to the login page.
    If there is an error, display an error message.
    If the request method is GET, display an empty signup form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
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