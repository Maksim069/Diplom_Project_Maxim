from rest_framework import serializers

from my_apps.question.error_messages import (
    QUESTION_NAME_LEN_ERROR_MESSAGE,
    NON_UNIQUE_QUESTION_NAME_ERROR_MESSAGE
)
from my_apps.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def validate_name(self, value):
        if Question.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                NON_UNIQUE_QUESTION_NAME_ERROR_MESSAGE
            )

        if len(value) < 3 or len(value) > 100:
            raise serializers.ValidationError(
                QUESTION_NAME_LEN_ERROR_MESSAGE
            )

        return value