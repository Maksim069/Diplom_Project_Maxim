from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from my_apps.answer_option.success_messages import (
    NEW_ANSWER_OPTION_CREATED_MESSAGE,
    ANSWER_OPTION_UPDATED_SUCCESSFULLY_MESSAGE,
    ANSWER_OPTION_WAS_DELETED_SUCCESSFUL,
)
from my_apps.answer_option.models import AnswerOption
from my_apps.answer_option.serializers import (
    AnswerOptionSerializer,
)


class AnswerOptionListGenericView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerOptionSerializer
    queryset = AnswerOption.objects.all()

    def get(self, request: Request, *args, **kwargs):
        answer_options = self.get_queryset()

        if answer_options:
            serializer = self.serializer_class(answer_options, many=True)

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
                    "message": NEW_ANSWER_OPTION_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


class RetrieveAnswerOptionGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerOptionSerializer

    def get_object(self):
        answer0ption_id = self.kwargs.get("answer0ption_id")

        answer0ption_obj = get_object_or_404(AnswerOption, id=answer0ption_id)

        return answer0ption_obj

    def get(self, request: Request, *args, **kwargs):
        answer0ption_obj = self.get_object()

        serializer = self.serializer_class(answer0ption_obj)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        answer0ption_obj = self.get_object()

        serializer = self.serializer_class(answer0ption_obj, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": ANSWER_OPTION_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        answer0ption_obj = self.get_object()

        answer0ption_obj.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=ANSWER_OPTION_WAS_DELETED_SUCCESSFUL
        )
