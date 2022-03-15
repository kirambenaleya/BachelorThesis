from unittest import TestCase
import numpy as np

from AlgorithmTeamFormation import create_vector
from AlgorithmTeamFormation import preprocess_data


class TestCreateVector(TestCase):
    def test_create_vector_empty_array(self):
        students = []
        self.assertIsNone(create_vector(students))

    def test_create_vector_correct_data(self):
        students = preprocess_data('student_data_test.csv', delimiter=';')
        students = create_vector(students)
        self.assertCountEqual(np.array([1, 22, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), students[0]['17-939-000']['vector'])
