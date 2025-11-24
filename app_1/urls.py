from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('indexblah/', views.indexblah, name='indexblah')
    path('indexblah/', views.PostList.as_view(), name = 'home'),
    path('index_2/', views.PostList2.as_view(), name = 'public posts')
]