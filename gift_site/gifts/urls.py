# gifts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:link_name>/', views.gift_list, name='gift_list'),
]

