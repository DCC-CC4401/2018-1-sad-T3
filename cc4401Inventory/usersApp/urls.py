from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('landingtest', views.landing_test, name='testlndng'),
    path('landing', views.landing, name='landing'),
    path('buscar/', views.buscar, name='buscar'),
]

