from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logIn/', views.logIn, name='blog-logIn'),
    path('signup/', views.signup, name='blog-signup'),
    path('post/<int:cat_id>/', views.post_show, name='blog-post-show'),
    path('post/create/', views.PostCreate.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='blog-post-Update'),
]

