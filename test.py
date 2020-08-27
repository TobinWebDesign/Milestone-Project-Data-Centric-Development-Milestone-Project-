from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

          def test_index(self):
                    tester = app.test_client(self)
                    response = tester.get('/', content_type='html/text')
                    self.assertEqual(response.status_code, 200)

          def test_add_recipe(self):
                    tester = app.test_client(self)
                    response = tester.get('/add_recipe', follow_redirects=True)
                    self.assertIn(b'Add Recipes', response.data)

          def test_search(self):
                    tester = app.test_client(self)
                    response = tester.get('/search', content_type='html/text')
                    self.assertEqual(response.status_code, 200)

          def test_all_recipes(self):
                    tester = app.test_client(self)
                    response = tester.get('/all_recipes', content_type='html/text')
                    self.assertEqual(response.status_code, 200)

if  __name__ == '__main__':
          unittest.main()