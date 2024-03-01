from django.db import models
from my_apps.surveys.models import Survey


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    QUESTION_TYPES = (
        ('single_choice', 'Single Choice'),
        ('multiple_chose', 'Multiple Choice'),
        ('text_answer', 'Text Answer'),
    )
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.name

    def count_by_question(self, question_name):
        try:
            question = Question.objects.get(name=question_name)
        except Question.DoesNotExist:
            return 0

        count = Survey.objects.filter(question=question).count()
        return count

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
