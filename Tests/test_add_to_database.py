from unittest import TestCase
from database_functions import add_survey_to_database, read_from_database


class TestAddToDatabase(TestCase):
    def test_add_to_database_valid_input(self):
        api_key = 'AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0'
        collection = u'Test'
        document = u'Test1'
        add_survey_to_database('Test111', 'Test222', 18, 'male', 'bachelor', 'major', '17-939-083',
                        '17-939-084', ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                                       '0', '0', '0', '0', '0'], 'kiram@gmx.ch', 'adminadmin123', api_key, collection,
                               document)
        dictionary = read_from_database('kiram@gmx.ch', 'adminadmin123', api_key, collection, document)
        self.assertEqual(dictionary['Email'], 'kiram@gmx.ch')
        self.assertEqual(dictionary['First Name'], 'Test111')
        self.assertEqual(dictionary['Last Name'], 'Test222')
        self.assertEqual(dictionary['Age'], 18)
        self.assertEqual(dictionary['Gender'], 'male')
        self.assertEqual(dictionary['Major/Minor'], 'major')
        self.assertEqual(dictionary['Bachelor/Master'], 'bachelor')
        self.assertEqual(dictionary['Schedule'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                                                  '0', '0', '0', '0', '0', '0', '0'])
        self.assertEqual(dictionary['Teammate'], '17-939-084')
        self.assertEqual(dictionary['Matriculation Number'], '17-939-083')
