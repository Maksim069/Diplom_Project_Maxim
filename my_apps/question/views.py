from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from my_apps.question.success_messages import (
    NEW_QUESTION_CREATED_MESSAGE,
    QUESTION_UPDATED_SUCCESSFULLY_MESSAGE,
    QUESTION_WAS_DELETED_SUCCESSFUL,
)
from my_apps.question.models import Question
from my_apps.question.serializers import (
    QuestionSerializer,
)


class QuestionListGenericView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request: Request, *args, **kwargs):
        questions = self.get_queryset()

        if questions:
            serializer = self.serializer_class(questions, many=True)

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
                    "message": NEW_QUESTION_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


class RetrieveQuestionGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_object(self):
        question_id = self.kwargs.get("question_id")

        question_obj = get_object_or_404(Question, id=question_id)

        return question_obj

    def get(self, request: Request, *args, **kwargs):
        question_obj = self.get_object()

        serializer = self.serializer_class(question_obj)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        question_obj = self.get_object()

        serializer = self.serializer_class(question_obj, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": QUESTION_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        question_obj = self.get_object()

        question_obj.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=QUESTION_WAS_DELETED_SUCCESSFUL
        )
