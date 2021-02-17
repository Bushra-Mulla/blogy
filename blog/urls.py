from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('logIn/', views.logIn, name='blog-logIn'),
    path('signup/', views.signup, name='blog-signup'),
]
