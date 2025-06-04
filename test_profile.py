import json
import os
import unittest
from datetime import datetime

class TestProfileJSON(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.path.join(os.path.dirname(__file__), 'profile.json')
        with open(path, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)

    def test_required_fields(self):
        required_fields = [
            'name', 'language', 'description', 'contacts',
            'created_at', 'updated_at'
        ]
        for field in required_fields:
            self.assertIn(field, self.data)

    def test_contacts_is_list(self):
        self.assertIsInstance(self.data.get('contacts'), list)

    def test_timestamp_format(self):
        for key in ['created_at', 'updated_at']:
            value = self.data.get(key)
            self.assertIsInstance(value, str)
            # basic ISO8601 check
            datetime.fromisoformat(value.replace('Z', '+00:00'))

if __name__ == '__main__':
    unittest.main()
