from django.shortcuts import render


def greeting(request):
    return render(
        request=request,
        template_name="questions/greeting.html"
    )


def show_user_info(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(
        request=request,
        template_name="questions/user_info.html",
        context=context
    )