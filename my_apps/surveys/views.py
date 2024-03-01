from django.shortcuts import render
from my_apps.surveys.models import Survey
from my_apps.user.models import User


def create_new_survey(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        Survey.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date
        )

    return render(
        request=request,
        template_name="questions/create_survey.html",
    )


def get_all_surveys(request):
    surveys = Survey.objects.all()
    context = {
        "surveys": surveys,
    }
    return render(
        request=request,
        template_name="questions/all_surveys.html",
        context=context
    )


def main(request):
    return render(
        request=request,
        template_name="questions/main.html"
    )


def show_user_info(request):
    users = request.user
    context = {
        "users": users,
    }
    return render(
        request=request,
        template_name="questions/user_info.html",
        context=context
    )
