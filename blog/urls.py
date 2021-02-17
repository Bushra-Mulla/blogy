from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logIn/', views.logIn, name='blog-logIn'),
    path('signup/', views.signup, name='blog-signup'),
    path('create/', views.PostCreate.as_view(), name='blog-post-create'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='blog-post-Update'),
]

