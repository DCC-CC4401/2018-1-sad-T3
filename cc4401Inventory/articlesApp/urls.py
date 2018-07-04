from django.urls import path

from . import views

app_name = 'list'
urlpatterns = [
    path('/<int:article_id>', views.article_data, name='article_data'),
    path('/<int:article_id>/edit', views.article_data_admin, name='article_data_admin'),
]
