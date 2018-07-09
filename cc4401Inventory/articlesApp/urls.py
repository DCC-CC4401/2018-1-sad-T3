from django.urls import path

from . import views

urlpatterns = [
    path('<int:article_id>', views.article_data, name='article_data'),
    path('<int:article_id>/edit', views.article_data_admin, name='article_data_admin'),
    path('<int:article_id>/edit_name', views.article_edit_name, name='article_edit_name'),
    path('<int:article_id>/edit_image', views.article_edit_image, name='article_edit_image'),
    path('<int:article_id>/edit_description', views.article_edit_description, name='article_edit_description'),
    path('request', views.article_request, name='article_request'),
]
