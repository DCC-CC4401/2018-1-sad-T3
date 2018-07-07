from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from mainApp.models import User
from django.http import HttpResponse


def login_page(request):
    if request.method == 'GET':
        return render(request, 'usersApp/login.html')
    if request.method == 'POST':
        pass


def login_user(request):

    username = request.POST['email']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        username = user.get_full_name()
        email = user.get_email()

        context = {'username': username,
                   'email' : email}
        #aca hay que redirigir a la pagina de inicio del usuario
        return render(request, 'usersApp/success.html', context=context)


    else:
        return HttpResponse("Error, invalid user")
        # Return an 'invalid login' error message.


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
