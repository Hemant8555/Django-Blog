from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import funding_request
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def profile(request, username):
    user_details = username
    active_user = str(request.user)


    return render(request, 'profile.html', {'user_details': username, 'active_user': str(request.user)})


def funding(request):
    if request.method == "POST":
        startup_name = request.POST['startup_name']
        startup_problem = request.POST['startup_problem']
        startup_solution = request.POST['startup_solution']
        stage = request.POST['stage']
        startup_registration = request.POST['startup_registration']

        funding_obj = funding_request(title=startup_name,
                                    stage=stage,
                                    problem=startup_problem,
                                    solution=startup_solution,
                                    company=startup_registration,
                                    )
        funding_obj.save()
        return HttpResponse('form submitted')

    else:
        return render(request, 'funding_page.html')


def leaderboard(request):
    projects = funding_request.objects.all()
    return render(request, 'leaderboard.html', {'projects': projects})


def team(request):
    users = User.objects.all()
    return render(request, 'team_page.html', {"users": users})
