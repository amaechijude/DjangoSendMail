from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    #path('room', views.room, name='room'),
    # path('signup', views.signup, name='signup'),
    # path('', views.login_user, name='login_user'),
    # path('logout_user', views.logout_user, name='logout_user'),
    path('sendmail', views.sendmail, name='sendmail'),
]