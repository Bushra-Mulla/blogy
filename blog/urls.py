from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),

]
=======
    path('', views.home, name='home'),
    path('logIn/', views.logIn, name='blog-logIn'),
    path('signup/', views.signup, name='blog-signup'),
]

>>>>>>> 433c13d5660322080174293daf43204426d84f2c
