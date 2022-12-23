from django.test import TestCase

from locations.models import Bookmark, Comment
# Create your tests here.

class Test_Comment(TestCase):
    def test_str(self):
        comment = Comment(text="my test string")
        self.assertEqual(str(comment),"my test string")