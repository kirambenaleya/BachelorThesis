from unittest import TestCase
from database_functions import check_if_survey_answered


class TestCheckIfSurveyAnswered(TestCase):
    def test_check_if_survey_answered_is_answered(self):
        email = 'test@test.test'
        dictionary = {
            'Email': 'test@test.test',
        }
        self.assertTrue(check_if_survey_answered(email, dictionary))

    def test_check_if_survey_answered_is_not_answered(self):
        email = 'test@test.test'
        dictionary = {
        }
        self.assertFalse(check_if_survey_answered(email, dictionary))

    def test_check_if_survey_answered_is_not_answered_wrong_email(self):
        email = 'test@test.test'
        dictionary = {
            'Email': 'testtest@test.test',
        }
        self.assertFalse(check_if_survey_answered(email, dictionary))
