from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # This specifies that the form is linked to the Book model.
        fields = ['title', 'author', 'published_date']


