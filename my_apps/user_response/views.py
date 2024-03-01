from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from my_apps.user_response.success_messages import (
    NEW_USER_RESPONSE_CREATED_MESSAGE,
    USER_RESPONSE_UPDATED_SUCCESSFULLY_MESSAGE,
    USER_RESPONSE_WAS_DELETED_SUCCESSFUL,
)
from my_apps.user_response.models import UserResponse
from my_apps.user_response.serializers import (
    UserResponseSerializer,
)


class UserResponseListGenericView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserResponseSerializer
    queryset = UserResponse.objects.all()

    def get(self, request: Request, *args, **kwargs):
        user_responses = self.get_queryset()

        if user_responses:
            serializer = self.serializer_class(user_responses, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "message": NEW_USER_RESPONSE_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


class RetrieveUserResponseGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserResponseSerializer

    def get_object(self):
        user_responses_id = self.kwargs.get("question_id")

        user_responses_obj = get_object_or_404(UserResponse, id=user_responses_id)

        return user_responses_obj

    def get(self, request: Request, *args, **kwargs):
        user_responses_obj = self.get_object()

        serializer = self.serializer_class(user_responses_obj)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        user_responses_obj = self.get_object()

        serializer = self.serializer_class(user_responses_obj, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": USER_RESPONSE_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        user_responses_obj = self.get_object()

        user_responses_obj.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=USER_RESPONSE_WAS_DELETED_SUCCESSFUL
        )
