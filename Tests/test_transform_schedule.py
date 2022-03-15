from unittest import TestCase
from database_functions import transform_schedule


class TestTransformSchedule(TestCase):
    def test_transform_schedule_none(self):
        schedule_part1 = ['None']
        schedule_part2 = ['None']
        schedule_part3 = ['None']
        self.assertEqual('---------------------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_transform_schedule_all(self):
        schedule_part1 = ['All']
        schedule_part2 = ['All']
        schedule_part3 = ['All']
        self.assertEqual('+++++++++++++++++++++', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_initial_monday(self):
        schedule_part1 = ['Monday']
        schedule_part2 = ['None']
        schedule_part3 = ['None']
        self.assertEqual('+--------------------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_initial_monday_second_array(self):
        schedule_part1 = ['None']
        schedule_part2 = ['Monday']
        schedule_part3 = ['None']
        self.assertEqual('-------+-------------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_initial_non_monday_second_array(self):
        schedule_part1 = ['None']
        schedule_part2 = ['Tuesday']
        schedule_part3 = ['None']
        self.assertEqual('--------+------------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_initial_non_monday(self):
        schedule_part1 = ['Tuesday']
        schedule_part2 = ['None']
        schedule_part3 = ['None']
        self.assertEqual('-+-------------------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_last_element_monday(self):
        schedule_part1 = ['None']
        schedule_part2 = ['None']
        schedule_part3 = ['Monday']
        self.assertEqual('--------------+------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_last_element_non_monday(self):
        schedule_part1 = ['None']
        schedule_part2 = ['None']
        schedule_part3 = ['Tuesday']
        self.assertEqual('---------------+-----', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_last_element_sunday(self):
        schedule_part1 = ['None']
        schedule_part2 = ['None']
        schedule_part3 = ['Sunday']
        self.assertEqual('--------------------+', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_second_element_smaller_index_than_first(self):
        schedule_part1 = ['Thursday']
        schedule_part2 = ['Monday']
        schedule_part3 = ['None']
        self.assertEqual('---+---+-------------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_second_element_multiple_elements_array(self):
        schedule_part1 = ['Thursday', 'Friday']
        schedule_part2 = ['Monday', 'Tuesday', 'Friday']
        schedule_part3 = ['None']
        self.assertEqual('---++--++--+---------', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_second_element_random_compositions(self):
        schedule_part1 = ['Thursday', 'Friday']
        schedule_part2 = ['None']
        schedule_part3 = ['Monday', 'Tuesday', 'Friday']
        self.assertEqual('---++---------++--+--', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_second_element_only_last_array(self):
        schedule_part1 = ['None']
        schedule_part2 = ['None']
        schedule_part3 = ['Monday', 'Tuesday', 'Wednesday', 'Friday']
        self.assertEqual('--------------+++-+--', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_second_element_all_arrays(self):
        schedule_part1 = ['Monday', 'Tuesday', 'Wednesday', 'Saturday']
        schedule_part2 = ['Monday', 'Tuesday', 'Wednesday', 'Saturday', 'Sunday']
        schedule_part3 = ['Monday', 'Tuesday', 'Wednesday', 'Friday']
        self.assertEqual('+++--+-+++--+++++-+--', transform_schedule(schedule_part1, schedule_part2, schedule_part3))

    def test_second_element_only_sundays(self):
        schedule_part1 = ['Sunday']
        schedule_part2 = ['Sunday']
        schedule_part3 = ['Sunday']
        self.assertEqual('------+------+------+', transform_schedule(schedule_part1, schedule_part2, schedule_part3))