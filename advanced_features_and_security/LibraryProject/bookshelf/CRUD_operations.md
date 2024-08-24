from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
Book object (1)
>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book)
Book object (1)
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> books = Book.objects.all()
>>> print(books)
<QuerySet []>