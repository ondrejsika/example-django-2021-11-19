from django.shortcuts import render, get_object_or_404
from .models import Author, Book

def index_view(request):
    return render(request, "example/index.html", {
        "authors": Author.objects.all().order_by("name"),
    })

def author_view(request, author_id):
    return render(request, "example/author.html", {
        "author": get_object_or_404(Author, id=author_id)
    })

def book_view(request, book_id):
    return render(request, "example/book.html", {
        "book": get_object_or_404(Book, id=book_id)
    })
