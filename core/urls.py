from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign', views.sign, name='sign'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('setting', views.setting, name='setting'),
    path('like_post', views.like_post, name="like_post"),
    path('create_post', views.create_post, name='create_post'),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('follow', views.follow, name="follow"),
    path('comment', views.comment, name="comment"),
    path('post_delete', views.post_delete, name='post_delete'),
    path('search', views.search, name="search"),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="reset_complete.html"), name="password_reset_complete"),
] 
