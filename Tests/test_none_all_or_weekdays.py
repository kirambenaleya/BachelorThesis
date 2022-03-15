from unittest import TestCase
from helping_functions import none_all_or_weekdays


class TestNoneAllOrWeekdays(TestCase):
    def test_none_all_or_weekdays_none(self):
        schedule = ['None']
        self.assertTrue(none_all_or_weekdays(schedule))

    def test_none_all_or_weekdays_all(self):
        schedule = ['All']
        self.assertTrue(none_all_or_weekdays(schedule))

    def test_none_all_or_weekdays_different_weekdays(self):
        schedule = ['Monday', 'Tuesday', 'Sunday']
        self.assertTrue(none_all_or_weekdays(schedule))

    def test_none_all_or_weekdays_wrong_input_all(self):
        schedule = ['All', 'Sunday']
        self.assertFalse(none_all_or_weekdays(schedule))

    def test_none_all_or_weekdays_wrong_input_none(self):
        schedule = ['None', 'Sunday']
        self.assertFalse(none_all_or_weekdays(schedule))

    def test_none_all_or_weekdays_wrong_input_none_all(self):
        schedule = ['None', 'All']
        self.assertFalse(none_all_or_weekdays(schedule))

    def test_none_all_or_weekdays_no_input(self):
        schedule = []
        self.assertFalse(none_all_or_weekdays(schedule))
