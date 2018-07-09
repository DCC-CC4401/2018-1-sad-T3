from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reservationsApp.models import Reservation
from loansApp.models import Loan
from articlesApp.models import Article
from spacesApp.models import Space
from mainApp.models import User


@login_required
def user_panel(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_panel.html', context)

@login_required
def items_panel(request):
    articles = Article.objects.all()
    spaces = Space.objects.all()
    context = {
        'articles': articles,
        'spaces': spaces
    }
    return render(request, 'items_panel.html', context)

@login_required
def actions_panel(request):
    reservations = Reservation.objects.all()
    loans = Loan.objects.all()
    context = {
        'reservations': reservations,
        'loans': loans
    }
    return render(request, 'actions_panel.html', context)
