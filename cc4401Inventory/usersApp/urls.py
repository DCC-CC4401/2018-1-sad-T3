from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.user_data, name='user_data'),
    path('signup/', views.signup, name='signup'),
    path('login_page/', views.login_page, name='login_page'),
    path('login/', views.login_submit, name='login'),
    path('signup/submit/', views.signup_submit, name='signup_submit')
]

