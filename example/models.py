from django.db import models
from django.db.models.base import Model

class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return "%s: %s" % (self.author.name, self.title)
