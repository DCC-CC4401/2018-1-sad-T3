from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.user_data, name='user_data'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login_page/', views.login_page, name='login_page'),
    path('login/', views.login_user, name='login'),
]

