from rest_framework import serializers

from my_apps.user_response.error_messages import (
    USER_RESPONSE_NAME_LEN_ERROR_MESSAGE,
    NON_UNIQUE_USER_RESPONSE_NAME_ERROR_MESSAGE
)
from my_apps.user_response.models import UserResponse


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = '__all__'

    def validate_name(self, value):
        if UserResponse.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                NON_UNIQUE_USER_RESPONSE_NAME_ERROR_MESSAGE
            )

        if len(value) < 3 or len(value) > 30:
            raise serializers.ValidationError(
                USER_RESPONSE_NAME_LEN_ERROR_MESSAGE
            )

        return value