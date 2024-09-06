from django.db import models

# Create your models here.
# The Author model represents the book authors in the system.
# Each author has a one-to-many relationship with books, where an author can write multiple books.

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# The Book model stores book information and is linked to an author through a foreign key.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title