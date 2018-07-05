from django.shortcuts import render, redirect
from mainApp.models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'usersApp/login.html')
    if request.method == 'POST':
        pass


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'usersApp/create_account.html')
    if request.method == 'POST':
        pass


def user_data(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, 'user_profile.html', context)
    except:
        redirect('/')
