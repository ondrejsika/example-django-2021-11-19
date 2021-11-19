from django.shortcuts import render
from .models import Author, Book

# Create your views here.
def index_view(request):
    return render(request, "example/index.html", {
        "authors": Author.objects.all().order_by("name"),
    })
