from rest_framework import serializers

from my_apps.answer_option.error_messages import (
    ANSWER_OPTION_NAME_LEN_ERROR_MESSAGE,
    NON_UNIQUE_ANSWER_OPTION_NAME_ERROR_MESSAGE
)
from my_apps.answer_option.models import AnswerOption


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = '__all__'

    def validate_name(self, value):
        if AnswerOption.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                NON_UNIQUE_ANSWER_OPTION_NAME_ERROR_MESSAGE
            )

        if len(value) < 3 or len(value) > 30:
            raise serializers.ValidationError(
                ANSWER_OPTION_NAME_LEN_ERROR_MESSAGE
            )

        return value