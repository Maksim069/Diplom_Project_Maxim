from django.urls import path

from my_apps.surveys.views import (
    get_all_surveys,
    main,
    create_new_survey
)


urlpatterns = [
    path('', main),
    path('CreateNewSurvey/', create_new_survey),
    path("AllSurveys1/", get_all_surveys),
    path('home/', main),
    # path('',),
]
