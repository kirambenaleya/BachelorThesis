from unittest import TestCase
from database_functions import sort_schedule


class TestSortSchedule(TestCase):
    def test_sort_schedule_all_empty(self):
        self.assertEqual(sort_schedule([], [], []), ([], [], []))

    def test_sort_schedule_none_empty(self):
        self.assertEqual(sort_schedule(['Monday', 'Tuesday'], ['Thursday', 'Friday', 'Monday'], ['Friday', 'Sunday',
                                                                                                 'Monday']),
                         (['Monday', 'Tuesday'], ['Monday', 'Thursday', 'Friday'], ['Monday', 'Friday', 'Sunday']))
