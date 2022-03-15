from unittest import TestCase

from AlgorithmTeamFormation import preprocess_data


class TestPreprocessData(TestCase):
    def test_preprocess_data_empty_file(self):
        self.assertIsNone(preprocess_data('empty_test.csv', ';'))

    def test_preprocess_data_right_data(self):
        students = preprocess_data('student_data_test.csv', ';')
        self.assertEqual(1, students[0]['17-939-000']['ID'])
        self.assertEqual('Klaus Habicht', students[0]['17-939-000']['Name'])
        self.assertEqual(1, students[0]['17-939-000']['Gender'])
        self.assertEqual(22, students[0]['17-939-000']['Age'])
        self.assertEqual(1, students[0]['17-939-000']['Education Level'])
        self.assertEqual(1, students[0]['17-939-000']['Major'])
        self.assertEqual(1, students[0]['17-939-000']['Attempt'])
        self.assertEqual(0, students[0]['17-939-000']['Teammate'])
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         students[0]['17-939-000']['Schedule'])

    def test_preprocess_data_teammates(self):
        students = preprocess_data('teammates_test.csv', ';')
        self.assertEqual(1, students[0]['17-939-000']['Teammate'])
        self.assertEqual(1, students[1]['17-939-001']['Teammate'])
