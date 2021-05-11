from unittest import TestCase
from unittest.mock import patch
import app 
from blog import Blog

class Apptest(TestCase):

    def test_print_menu(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test','Test author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('Test by Test author (0 post)')

    def test_input(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU)

    def test_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test','Test author')
            app.create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

