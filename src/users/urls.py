from django.urls import path
from . import views


urlpatterns = [
    path('homepage', views.homepage, name=""),

    path('register', views.register, name="register"),

    path('login', views.login_user, name="login_user"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),
]
