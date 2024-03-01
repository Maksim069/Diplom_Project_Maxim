from django import forms
from django.forms import fields, ModelForm, ModelChoiceField
from django.contrib.auth.models import User
from my_apps.question.models import (
    Question
)
from my_apps.answer_option.models import (
    AnswerOption
)
from my_apps.user_response.models import (
    UserResponse
)
from my_apps.surveys.models import (
    Survey
)


class CreateSurveysForm(ModelForm):
    title = fields.CharField(max_length=30)
    description = fields.CharField(max_length=1500, widget=fields.Textarea)
    creator = ModelChoiceField(queryset=User.objects.all())
    question = ModelChoiceField(queryset=Question.objects.all())
    answer_option = ModelChoiceField(queryset=AnswerOption.objects.all())
    user_response = ModelChoiceField(queryset=UserResponse.objects.all())
    start_date = fields.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'data'})
    )
    end_date = fields.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'data'})
    )
    is_active = fields.BooleanField()

    class Meta:
        model = Survey
        fields = '__all__'
