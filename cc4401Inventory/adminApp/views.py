from django.shortcuts import render


def user_panel(request):
    return render(request, 'user_panel.html')


def items_panel(request):
    return render(request, 'items_panel.html')


def actions_panel(request):
    return render(request, 'actions_panel.html')
