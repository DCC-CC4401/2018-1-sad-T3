from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from mainApp.models import User
from django.http import HttpResponse, HttpResponseRedirect


def login_page(request):
    if request.method == 'GET':
        return render(request, 'usersApp/login.html')
    if request.method == 'POST':
        pass

#se llama cuando se envia el formulario de login
def login_submit(request):

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


#se llama cuando se quiere acceder a la pagina de creacion de cuentas
def signup(request):
    if request.method == 'GET':
        return render(request, 'usersApp/create_account.html')
    if request.method == 'POST':
        pass

#se llama cuando se manda el formulario de creacion de cuentas
def signup_submit(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first_name, email=email, password=password)

        return render(request, 'usersApp/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.path_info)


def user_data(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, 'user_profile.html', context)
    except:
        redirect('/')
