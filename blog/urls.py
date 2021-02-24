from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import context_processors
# from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('logIn/', auth_views.LoginView.as_view(template_name='logIn.html'), name='logIn'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name="logout"),
    
    path('profile/', views.profile, name="profile"),
    path('profile/create', views.ProfileCreate.as_view(
        template_name='user/profile_form.html'), name='user-profile-create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(template_name='user/profile_form.html'),
         name='user-profile-update'),
    path('profile/<int:user_id>', views.authoreProfile, name="profile"),
    path('profile/<int:user_id>/posts/', views.authorePosts, name="authorePosts"),
    path('profile/<int:user_id>/likes/', views.authoreLikes, name="authoreLikes"),
    path('profile/<int:user_id>/comments/',
         views.authoreComments, name="usercomments"),


    path('user/likes/', views.likes_list, name='blog_like_list'),
    path('user/posts/', views.userPostsList, name='userPostsList'),
    path('user/posts/published/', views.userPublishedPostsList,
         name='userPublishedPostsList'),
    path('user/posts/notPublished/', views.userNotPublishedPostsList,
         name='userNotPublishedPostsList'),
    path('user/posts/refused/', views.userRefusedPostsList,
         name='userRefusedPostsList'),
    path('user/comments',  views.comment_list, name='comment_list'),
    path('user/posts/draft/', views.userDraftPostsList,
         name='userDraftPostsList'),


    path('category/create/', views.categoryCreate.as_view(
        template_name='category/categorys_form.html'), name="categoryCreate"),
    path('category/<int:pk>/',
         views.category_view, name='blog-category_view'),


    path('post/<int:post_id>/', views.post_show, name='blog-post-show'),
    path('post/create/', views.PostCreate.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(),
         name='blog-post-Update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(),
         name='blog-post-delete'),


    path('like/', views.likeview, name='like_post'),
    path('comment/',  views.comments, name='comment'),


    path('report/<int:post_id>/create/', views.reportCreate.as_view(
        template_name='report/reports_form.html'), name="reportCreate"),
    path('reports/', views.reports, name="reports"),
    path('reports/<int:report_id>/', views.reportDetails, name="reportDetails"),
    path('reports/<int:report_id>/archived',
         views.archiveReport, name="archiveReport"),
    path('reports/notArchived',
         views.notArchivedReport, name="notArchivedReport"),
    path('reports/archived',
         views.archivedReport, name="archivedReport"),

    # Archived == notpublish  all=published NotArchived = refused
    path('published/', views.publish, name='blog-published'),
    path('published/<int:post_id>/', views.postDetails, name="postDetails"),
    path('published/<int:post_id>/notpublish',
         views.update_published, name="update_published"),
    path('published/<int:post_id>/refused',
         views.update_refuse, name="update_refuse"),
    path('published/refused',
         views.refused, name="refused"),
    path('published/notpublish',
         views.notpublish, name="notpublish"),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'), name='password_reset_complete'),


    path('search/', views.search, name='search'),
#     path('admin/', admin.site.urls, name='admin'),
]
