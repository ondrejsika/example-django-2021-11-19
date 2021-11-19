from django.contrib import admin
from django.db import models
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_filter = (
        "author",
    )
    list_display = (
        "title",
        "author",
    )

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
