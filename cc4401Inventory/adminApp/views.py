from django.shortcuts import render
from reservationsApp.models import Reservation
from loansApp.models import Loan


def user_panel(request):
    return render(request, 'user_panel.html')


def items_panel(request):
    return render(request, 'items_panel.html')


def actions_panel(request):
    reservations = Reservation.objects.all()
    loans = Loan.objects.all()
    context = {
        'reservations': reservations,
        'loans': loans
    }
    return render(request, 'actions_panel.html', context)
