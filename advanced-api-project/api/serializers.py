from rest_framework import serializers
from .models import Book
import datetime

# The BookSerializer serializes book fields, including the author.
# Custom validation is applied to ensure that the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

from .models import Author
from .serializers import BookSerializer

# The AuthorSerializer serializes author information and includes nested books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
