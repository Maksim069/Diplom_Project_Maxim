from django.urls import path

from my_apps.answer_option.views import (
    AnswerOptionListGenericView,
    RetrieveAnswerOptionGenericView
)


urlpatterns = [
    path("", AnswerOptionListGenericView.as_view()),
    path("<int:answerOption_id>/", RetrieveAnswerOptionGenericView.as_view()),
]
