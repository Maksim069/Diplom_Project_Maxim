from django.urls import path

from my_apps.question.views import (
    QuestionListGenericView,
    RetrieveQuestionGenericView
)


urlpatterns = [
    path("", QuestionListGenericView.as_view()),
    path("<int:question_id>/", RetrieveQuestionGenericView.as_view()),
]
