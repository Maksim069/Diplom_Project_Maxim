from django.urls import path

from my_apps.questions.views import (
    greeting,
)


urlpatterns = [
    path("", greeting),
]
