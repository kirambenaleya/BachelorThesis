from unittest import TestCase

from AlgorithmTeamFormation import convert_to_tuples
from AlgorithmTeamFormation import create_vector
from AlgorithmTeamFormation import preprocess_data


class TestConvertToTuples(TestCase):
    def test_convert_to_tuples_empty_list(self):
        students = []
        self.assertIsNone(convert_to_tuples(students))

    def test_convert_to_tuples_normal_list(self):
        students = preprocess_data('student_data_test.csv', delimiter=';')
        students = create_vector(students)
        students = convert_to_tuples(students)
        part1, part2 = students[0]
        self.assertEqual(part1, '17-939-000')
        self.assertCountEqual(part2, [1, 22, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

