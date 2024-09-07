# The BookListView allows users to retrieve all books.
# Unauthenticated users have read-only access.
class BookListView(generics.ListAPIView):
    ...

# The BookDetailView allows users to retrieve a specific book by ID.
# Unauthenticated users have read-only access.
class BookDetailView(generics.RetrieveAPIView):
    ...

# The BookCreateView allows authenticated users to create a new book.
# It checks permissions to ensure only authenticated users can create a book.
class BookCreateView(generics.CreateAPIView):
    ...

# The BookUpdateView allows authenticated users to modify an existing book.
class BookUpdateView(generics.UpdateAPIView):
    ...

# The BookDeleteView allows authenticated users to delete a book.
class BookDeleteView(generics.DestroyAPIView):
    ...

In api/urls.py, configured URL patterns to connect the views with specific endpoints.

perform_create(): This method is called during the POST request when a new book is being created. You can add custom validation (e.g., checking if the publication year is valid) and automatically set the author based on the logged-in user.

perform_update(): This method is called when an existing book is being updated (PUT request). You can add extra validation (e.g., locking the author field from being updated) and perform checks like ensuring the publication_year is valid.

- Filtering:
    - Filter by title: /api/books/?title=SomeTitle
    - Filter by author: /api/books/?author__name=AuthorName
    - Filter by publication year: /api/books/?publication_year=2023

- Searching:
    - Search by title or author: /api/books/?search=SearchTerm

- Ordering:
    - Order by title: /api/books/?ordering=title
    - Order by publication year (descending): /api/books/?ordering=-publication_year

Testing Strategy

This project includes unit tests for the Book API to verify that:
- CRUD operations (Create, Retrieve, Update, Delete) work correctly.
- Filtering, searching, and ordering functions behave as expected.
- Permissions and authentication are correctly enforced on endpoints.

### Running the Tests

Use the following command to run the tests:

```bash
python manage.py test api