from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def  test_post_create(self):
        p = Post('Test','Test Content')

        self.assertEqual('Test',p.title)
        self.assertEqual('Test Content',p.content)

