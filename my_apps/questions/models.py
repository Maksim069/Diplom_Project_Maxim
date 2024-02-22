from django.db import models


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.TextField()
    QUESTION_TYPES = (
        ('single_choice', 'Single Choice'),
        ('multiple_choice', 'Multiple Choice'),
        ('text_answer', 'Text Answer'),
    )
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    @classmethod
    def create_question(cls, survey, text, question_type):
        question = cls(survey=survey, text=text, question_type=question_type)
        question.save()
        return question


class AnswerOption(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()


class UserResponse(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(AnswerOption, null=True, blank=True, on_delete=models.CASCADE)
    text_response = models.TextField(blank=True)
    user_id = models.IntegerField()