from django.urls import path, include
from my_apps.questions.views import (
    show_user_info,
)


urlpatterns = [
    path('user_info/', show_user_info),
]
