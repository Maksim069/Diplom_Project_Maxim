from django.db import models
from my_apps.question.models import Question
from my_apps.surveys.models import Survey


class AnswerOption(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def count_by_anwer_option(self, answer_option_name):
        try:
            answer_option = AnswerOption.objects.get(name=answer_option_name)
        except AnswerOption.DoesNotExist:
            return 0

        count = Survey.objects.filter(answer_option=answer_option).count()
        return count

    class Meta:
        verbose_name = 'AnswerOption'
        verbose_name_plural = 'AnswerOptions'
