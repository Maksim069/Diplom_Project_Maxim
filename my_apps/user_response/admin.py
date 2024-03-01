from django.contrib import admin

from my_apps.user_response.models import UserResponse


@admin.register(UserResponse)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

