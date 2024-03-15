from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('message/', views.message, name='message'),
    path('adduser/', views.adduser, name='adduser'),
    path('signin/', views.signin, name='signin'),
]
