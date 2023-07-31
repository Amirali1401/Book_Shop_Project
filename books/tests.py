# from django.test import TestCase
# from django.shortcuts import reverse
# from django.contrib.auth.models import User
#
# from .models import Book
# # # Create your tests here.
#
# class BookTest(TestCase):
#
#     def setUp(self):
#         self.user1 = User.objects.create(username = 'mahsa')
#         self.book1  = Book.objects.create(user = self.user1 , name = 'book1' , description = 'This is book1')
#
#
#     def test_list_books_url_by_name(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code , 302)
#
#
#     def test_detail_books_url_by_name(self):
#         response = self.client.get(reverse('detail_books' , args=[self.book1.id]))
#         self.assertEqual(response.status_code , 302)
#
#
#     def test_detail_books_404_url(self):
#             response = self.client.get(reverse('detail_books' ,args=[900]))
#             return self.asserEqual(response.status_code , 404)
