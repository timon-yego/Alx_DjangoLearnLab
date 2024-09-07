from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User  # Import User model
from api.models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create an Author and Book for testing
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2021, author=self.author)
    
    def test_create_book(self):
        url = reverse('book-list')  # URL for book list/create
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Check if new book was created

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})  # URL for retrieving a single book
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})  # URL for updating the book
        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Reload the book from the database
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})  # URL for deleting the book
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Ensure the book is deleted

    def test_filter_books_by_title(self):
        url = f"{reverse('book-list')}?title=Test Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_search_books(self):
        url = f"{reverse('book-list')}?search=Test"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn('Test Book', response.data[0]['title'])

    def test_order_books_by_publication_year(self):
        Book.objects.create(title="Older Book", publication_year=2000, author=self.author)
        url = f"{reverse('book-list')}?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2000)  # Oldest book first
