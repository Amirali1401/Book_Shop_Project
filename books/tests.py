from django.test import TestCase

from .models import Book
# Create your tests here.

class BookTest(TestCase):

    def setUp(self):
         Book.objects.create(name = 'book1'  ,description='This is a book1')
         Book.objects.create(name = 'book2' , description = 'This is a book2')


    def test_tell_name_books(self):
        book_1 = Book.objects.get(name = 'book1')
        book_2 = Book.objects.get(name = 'book2')
        self.assertEqual(book_1.tell_name() , 'please tell book1')
        self.assertEqual(book_2.tell_name() , 'please tell book2')
