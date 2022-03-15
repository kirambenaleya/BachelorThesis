from unittest import TestCase

import numpy as np

from AlgorithmTeamFormation import same_availability


class TestSameAvailability(TestCase):
    def test_same_availability_student_none(self):
        self.assertEqual(0, same_availability(None, None))

    def test_same_availability_student_valid_input_no_matches(self):
        student1 = ('17-939-083', np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                            0, 0]))
        student2 = ('17-939-083', np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
                                            0, 0]))
        self.assertEqual(0, same_availability(student1, student2))

    def test_same_availability_student_valid_input_with_matches(self):
        student1 = ('17-939-083', np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                                            1, 1]))
        student2 = ('17-939-083', np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1,
                                            1, 1]))
        self.assertEqual(3, same_availability(student1, student2))
