from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.user_data, name='user_data'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
]

