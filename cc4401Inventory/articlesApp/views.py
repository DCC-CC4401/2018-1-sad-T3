from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    #items = Item.objects.all()
    #context = {'items': items}
    return render(request, 'articlesApp.html')