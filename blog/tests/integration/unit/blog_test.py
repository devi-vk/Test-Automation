from unittest import TestCase
from blog import Blog

class Blogtest(TestCase):
    def test_blog_create(self):
        b = Blog('Title','Name')
        
        self.assertEqual('Title', b.title)
        self.assertEqual('Name', b.author)
        self.assertListEqual([], b.posts)

    def test___repr__(self):
        b = Blog('Title','Name')
        b2 = Blog('Learning','Dave')

        self.assertEqual(b.__repr__(), 'Title by Name (0 post)')
        self.assertEqual(b2.__repr__(), 'Learning by Dave (0 post)')

    def test_multiple_posts(self):
        b = Blog('Title','Name')
        b.posts = ['post']
        b1 = Blog('Learning','Dave')
        b1.posts = ['post1','post2','post3']
        self.assertEqual(b.__repr__(), 'Title by Name (1 post)')
        self.assertEqual(b1.__repr__(), 'Learning by Dave (3 posts)')

        