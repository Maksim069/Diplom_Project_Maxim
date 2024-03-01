from django.db import models
from my_apps.question.models import Question
from my_apps.answer_option.models import AnswerOption
from my_apps.surveys.models import Survey


class UserResponse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True
    )
    question = models.ManyToManyField(Question)
    selected_option = models.ForeignKey(
        AnswerOption,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    text_response = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def count_by_user_response(self, user_response_name):
        try:
            user_response = UserResponse.objects.get(name=user_response_name)
        except UserResponse.DoesNotExist:
            return 0

        count = Survey.objects.filter(user_response=user_response).count()
        return count

    class Meta:
        verbose_name = 'UserResponse'
        verbose_name_plural = 'UserResponses'
