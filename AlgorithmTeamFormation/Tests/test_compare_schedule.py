from unittest import TestCase
import numpy as np

from AlgorithmTeamFormation import compare_schedule


class TestCompareSchedule(TestCase):
    def test_compare_schedule_all_zeros(self):
        schedule_1 = np.array([0, 0, 0])
        schedule_2 = np.array([0, 0, 0])
        self.assertCountEqual(np.array([0, 0, 0]), compare_schedule(schedule_1, schedule_2))

    def test_compare_schedule_not_all_zeros(self):
        schedule_1 = np.array([0, 1, 1])
        schedule_2 = np.array([0, 1, 1])
        self.assertCountEqual(np.array([0, 1, 1]), compare_schedule(schedule_1, schedule_2))

    def test_compare_schedule_no_similarities(self):
        schedule_1 = np.array([0, 0, 1])
        schedule_2 = np.array([0, 1, 0])
        self.assertCountEqual(np.array([0, 0, 0]), compare_schedule(schedule_1, schedule_2))
