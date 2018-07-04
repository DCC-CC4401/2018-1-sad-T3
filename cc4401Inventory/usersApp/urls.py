from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/articulos/buscar/', views.buscar, name='buscar'),
    path('user/articulos/', views.landing_articulos, name='articulos'),
    path('user/espacios/', views.landing_espacios, name='espacios'),
]

