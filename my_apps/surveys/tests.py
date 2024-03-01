from django.test import TestCase
from datetime import date
from my_apps.surveys.models import Survey, Question, AnswerOption, UserResponse


class ModelsTestCase(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        survey = Survey.objects.create(
            title='Test Survey',
            description='This is a test survey',
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 31),
            is_active=True
        )
        question = Question.objects.create(
            survey=survey,
            text='What is your favorite color?',
            question_type='single_choice'
        )
        option1 = AnswerOption.objects.create(
            question=question,
            text='Red'
        )
        option2 = AnswerOption.objects.create(
            question=question,
            text='Blue'
        )
        response = UserResponse.objects.create(
            question=question,
            selected_option=option1,
            text_response='',
            user_id=1
        )

    def test_survey_model(self):
        survey = Survey.objects.get(title='Test Survey')
        self.assertEqual(survey.description, 'This is a test survey')
        self.assertEqual(survey.start_date, date(2022, 1, 1))
        self.assertEqual(survey.end_date, date(2022, 1, 31))
        self.assertTrue(survey.is_active)

    def test_question_model(self):
        question = Question.objects.get(text='What is your favorite color?')
        self.assertEqual(question.survey.title, 'Test Survey')
        self.assertEqual(question.question_type, 'single_choice')

    def test_answer_option_model(self):
        option1 = AnswerOption.objects.get(text='Red')
        option2 = AnswerOption.objects.get(text='Blue')
        self.assertEqual(option1.question.text, 'What is your favorite color?')
        self.assertEqual(option2.question.text, 'What is your favorite color?')

    def test_user_response_model(self):
        response = UserResponse.objects.get(user_id=1)
        self.assertEqual(response.question.text, 'What is your favorite color?')
        self.assertEqual(response.selected_option.text, 'Red')
        self.assertEqual(response.text_response, '')
        self.assertEqual(response.user_id, 1)
