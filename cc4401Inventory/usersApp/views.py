from django.shortcuts import render

#hay que importar los modelos


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

def landing_articulos(request):
    context = {}
    return render(request, 'articulos.html', context)

def landing_espacios(request):
    context = {}
    return render(request, 'espacios.html', context)

def landing_test(request):
    context = {}
    return render(request, 'usersApp/landing_user.html', context)

def landing_search(request, productos):
    if not productos:
        return landing_articulos(request)
    else:
        context = {'productos' : productos}
        return render(request, 'urlbleh', context)


def buscar(request):

    if request.method == "GET":

        productos = None
        # TODO: REALIZAR BUSQUEDA DE LOS PRODUCTOS

        #Una vez obtenidos los productos, mandar el queryset por el context
        # productos = "resultado de la cosita"

        return landing_search(request, productos)


def get_spaces(request):

        return landing_espacios(request)
