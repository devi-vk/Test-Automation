from unittest import TestCase
from blog import Blog

class Blog_inter_Test(TestCase):
    def test_blog_inter(self):
        b = Blog('Title','Name')
        b.create_post('Test post', 'Test content')

        self.assertEqual(len(b.posts),1)
        self.assertEqual(b.posts[0].title,'Test post')
        self.assertEqual(b.posts[0].content,'Test content')

    def test_json_emptypost(self):
        b = Blog('Title','Name')
        
        expected = {'Title': 'Title',
                    'Author': 'Name',
                    'posts': []}
        self.assertEqual(expected,b.json()) 

    def test_json(self):
        b = Blog('Title','Name')
        b.create_post('Test post','Test content')

        expected = {'Title': 'Title',
                    'Author': 'Name',
                    'posts': [{'title':'Test post',
                               'content':'Test content'
                               }
                              ]
                    }

        self.assertDictEqual(expected,b.json())        
