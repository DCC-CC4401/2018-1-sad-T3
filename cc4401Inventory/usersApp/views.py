from django.shortcuts import render

# Create your views here.

def landing_user(request):

    return render(request, 'usersApp/landing_user.html')

def login(request):
    return render(request, 'usersApp/login.html')

def create_account(request):
    return render(request, 'usersApp/create_account.html')

def index(request):
    context = {}
    return render(request, 'user_profile.html', context)

