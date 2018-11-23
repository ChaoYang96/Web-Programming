from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log/', views.log, name='log'),
    path('register/', views.register, name='register'),
    path('newUser/', views.newUser, name='newUser')
]
