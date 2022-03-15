from unittest import TestCase

from AlgorithmTeamFormation import determine_group_sizes


class TestDetermineGroupSizes(TestCase):
    def test_determine_group_wrong_inputs(self):
        with self.assertRaises(Exception): determine_group_sizes('string', 10)
        with self.assertRaises(Exception): determine_group_sizes(10, 0)
        with self.assertRaises(Exception): determine_group_sizes(10, -3)
        with self.assertRaises(Exception): determine_group_sizes(0, 2)
        with self.assertRaises(Exception): determine_group_sizes(-10, 3)

    def test_determine_group_valid_input(self):
        students = 10
        maximum = 3
        self.assertCountEqual([3, 3, 2, 2], determine_group_sizes(students, maximum))
