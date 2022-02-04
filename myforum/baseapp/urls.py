from django.urls import path

from . import views

app_name = 'baseapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create'),
    path('detail/<slug:slug>/', views.detail_post, name='detail'),
    path('edit/<slug:slug>/', views.edit_post, name='edit'),
    path('delete/<slug:slug>/', views.delete_post, name='delete'),
    path('category/<str:category>/', views.home, name='category')
]
