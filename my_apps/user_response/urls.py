from django.urls import path

from my_apps.user_response.views import (
    UserResponseListGenericView,
    RetrieveUserResponseGenericView
)


urlpatterns = [
    path("", UserResponseListGenericView.as_view()),
    path("<int:userResponse_id>/", RetrieveUserResponseGenericView.as_view()),
]
