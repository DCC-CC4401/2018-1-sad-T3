from django.shortcuts import render

#hay que importar los modelos
from articlesApp.models import Article

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
        context = {'productos' : productos,
                   'colores' : {'D': '#009900',
                                'R': '#ffcc00',
                                'P': '#3333cc',
                                'L': '#cc0000'}
                   }
        print(productos)
        return render(request, 'articulos.html', context)


def buscar(request):

    if request.method == "GET":
        query = request.GET['query']
        a_type = "filo"
        a_state = "A" if (request.GET['estado'] == "A") else request.GET['estado']

        # TODO: REALIZAR BUSQUEDA DE LOS PRODUCTOS

        if not (a_state == "A"):
            articles = Article.objects.filter(state=a_state,name__icontains=query.lower())
        else:
            articles = Article.objects.filter(name__icontains=query.lower())

        productos = None if (request.GET['query'] == "") else articles
        return landing_search(request, productos)


def get_spaces(request):

        return landing_espacios(request)
