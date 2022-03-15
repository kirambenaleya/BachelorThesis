from unittest import TestCase
from database_functions import read_from_database


class TestReadFromDatabase(TestCase):
    def test_read_from_database_none(self):
        api_key = 'AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0'
        collection = u'Test'
        document = u'Test123'
        dictionary = read_from_database('kiram@gmx.ch', 'adminadmin123', api_key, collection, document)
        self.assertEqual(None, dictionary)
