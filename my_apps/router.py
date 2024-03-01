from django.urls import path, include

urlpatterns = [
    path('', include('my_apps.surveys.urls')),
    path('home/', include('my_apps.surveys.urls')),
    path("users/", include('my_apps.user.urls')),
    path("answerOptions/", include('my_apps.answer_option.urls')),
    path("questions/", include('my_apps.question.urls')),
    path("surveys/", include('my_apps.surveys.urls')),
    path("userResponses/", include('my_apps.user_response.urls')),
]
