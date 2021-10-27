# tests.py
import unittest
import os
import json
from app import create_app, db



class TestFunctions(unittest.TestCase):
 “””Test case for the client methods.”””

    def setup(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        # Test of Output function
        def test_output(self):
            my_app.books = []
            resp = self.app.get('/api/get/data/2014')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.content_type, 'application/json')
            content = json.loads(resp.get_data(as_text=True))
            self.assertEqual(len(content), 0)
            self.assertEqual(content, [])

if __name__ == ‘__main__’:
      tests.main()