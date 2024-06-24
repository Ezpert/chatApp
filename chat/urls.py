from django.urls import path
from chatApp.chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatty/', views.chatty, name='chatty'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home')

]
