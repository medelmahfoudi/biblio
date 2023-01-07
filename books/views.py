from django.shortcuts import render
from .models import Book
from django.conf import settings


def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'media_url': settings.MEDIA_URL,
    }

    return render(request, 'books/index.html', context)