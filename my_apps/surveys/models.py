from django.db import models
from my_apps.user.models import User


class Survey(models.Model):
    id = (
        models.AutoField(primary_key=True)
    )
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(
        max_length=1500,
        verbose_name="task details",
        default="Here you can add your description..."
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    date_started = models.DateField(
        help_text="День, когда задача должна начаться",
        blank=True,
        null=True
    )
    deadline = models.DateField(
        help_text="День, когда задача должна быть выполнена",
        blank=True,
        null=True
    )
    false = False
    is_active = models.BooleanField(
        default=false
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title[:6]}..."

    # def count_by_question(self, question_name):
    #     try:
    #         question = Question.objects.get(name=question_name)
    #     except Question.DoesNotExist:
    #         return 0
    #
    #     count = Survey.objects.filter(question=question).count()
    #     return count

    # def count_by_anwer_option(self, answer_option_name):
    #     try:
    #         answer_option = AnswerOption.objects.get(name=answer_option_name)
    #     except AnswerOption.DoesNotExist:
    #         return 0
    #
    #     count = Survey.objects.filter(answer_option=answer_option).count()
    #     return count

    # def count_by_user_response(self, user_response_name):
    #     try:
    #         user_response = UserResponse.objects.get(name=user_response_name)
    #     except UserResponse.DoesNotExist:
    #         return 0
    #
    #     count = Survey.objects.filter(user_response=user_response).count()
    #     return count

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"