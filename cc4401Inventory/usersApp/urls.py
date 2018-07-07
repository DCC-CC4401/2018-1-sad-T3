from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.user_data, name='user_data'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('login/submit/', views.login_submit, name='login_submit'),
    path('signup/submit/', views.signup_submit, name='signup_submit'),
    path('logout/', views.logout_view, name='logout')
]

