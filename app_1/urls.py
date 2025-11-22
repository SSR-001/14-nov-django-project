from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indexblah/', views.indexblah, name='indexblah')
]