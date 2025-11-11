from django.shortcuts import render


def index(request):
    """Simple homepage view for the cookies app."""
    return render(request, 'cookies/index.html', {'message': 'Welcome to The Pink Cookie Sheet!'})
