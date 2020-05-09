from django.test import TestCase
from rest_framework.test import APIRequestFactory
from datetime import date

# Create your tests here.
class RestTesting(TestCase):

    def setUp(self):
        name = 'TestingRest'
        from book_visualizer.models import User
        self.user = User.objects.create_user(username=name, email='user@example.com', password='TestingPassword123')
        self.user.save()
        from book_visualizer.models import Book
        self.book = Book('1234', 'Some title', 'Author Example', date.today(), 'Publisher Example', 'Summary here')
        self.book.save()
    
    def test_get_comments(self):
        pass

    
