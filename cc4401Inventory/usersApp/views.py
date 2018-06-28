from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'user_profile.html', context)

def landing(request):
    context = {}
    return render(request, 'landing.html', context)

def landing_test(request):
    context = {}
    return render(request, 'usersApp/landing_user.html', context)


def buscar(request):

    if request.method == "POST":
        return landing_test(request)
    context = {}
    return landing(request)


