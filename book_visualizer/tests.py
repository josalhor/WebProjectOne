from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from collections import namedtuple
from book_visualizer.models import User, Book, Comment
from django.utils import timezone

# Create your tests here.
class RestTesting(APITestCase):

    CommentTemplate = namedtuple('Comment', 'title stars body based_on')
    comments = [
        CommentTemplate('Title One', '3', 'This is a long body comment1', '1234'),
        CommentTemplate('Title Two', '5', 'This is a long body comment2', '1235')
    ]

    def setUp(self):
        name = 'TestingRest'
        pasw = 'TestingPassword123'
        self.user = User.objects.create_user(username=name, email='user@example.com', password=pasw)
        self.user.save()
        self.assertTrue(self.client.login(username=name, password=pasw))
        self.book1 = Book('1234', 'Some title1', 'Author Example', timezone.now(), 'Publisher Example', 'Summary here')
        self.book1.save()
        self.book2 = Book('1235', 'Some title2', 'Author Example', timezone.now(), 'Publisher Example', 'Summary here')
        self.book2.save()
    
    def test_no_comments(self):
        response = self.client.get('/api/comments/', format='json')
        self.assertTrue(response.data == [])

    @staticmethod
    def compare_response_template(item_response, instance_template):
        for field in instance_template._fields:
            if item_response[field] != getattr(instance_template, field):
                return False
        return True

    def test_post_comments(self):
        for comment in RestTesting.comments:
            response = self.client.post(
                '/api/comments/',
                {
                    "stars": comment.stars,
                    "title": comment.title,
                    "body": comment.body,
                    "based_on": comment.based_on
                }, format='json')
            self.assertTrue(response.data['body'] == comment.body)
            self.assertTrue(response.data['title'] == comment.title)
            self.assertTrue(response.data['stars'] == comment.stars)
        response = self.client.get('/api/comments/', format='json')
        for comment in RestTesting.comments:
            found = False
            for response_comment in response.data:
                if RestTesting.compare_response_template(response_comment, comment):
                    found = True
                    break
            self.assertTrue(found)
        Comment.objects.all().delete()

    def test_delete_comments(self):
        for i, comment in enumerate(RestTesting.comments):
            new_comment = Comment(i, comment.title, comment.body, comment.stars, timezone.now(), self.user.id, comment.based_on)
            new_comment.save()
        for comment in RestTesting.comments:
            response = self.client.delete(f'/api/comments/{comment.based_on}/', format='json')
        response = self.client.get('/api/comments/', format='json')
        self.assertTrue(response.data == [])

    def test_wish_post(self):
        self.assertTrue(self.user.wishes.count() == 0)
        self.client.post('/api/wishes/', {"isbn": self.book1.isbn}, format='json')
        self.client.post('/api/wishes/', {"isbn": self.book2.isbn}, format='json')
        self.assertTrue(self.user.wishes.count() == 2)
        self.user.wishes.clear()
    
    def test_wish_delete(self):
        self.assertTrue(self.user.wishes.count() == 0)
        self.user.wishes.add(self.book1)
        self.user.wishes.add(self.book2)
        self.assertTrue(self.user.wishes.count() == 2)
        self.client.delete(f'/api/wishes/{self.book1.isbn}/', format='json')
        self.client.delete(f'/api/wishes/{self.book2.isbn}/', format='json')
        self.assertTrue(self.user.wishes.count() == 0)
