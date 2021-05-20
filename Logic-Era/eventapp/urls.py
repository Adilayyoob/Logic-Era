from django.urls import path
from . import views
urlpatterns = [
    path("",views.main,name='main'),
    path("home/<str:us>/",views.home,name='home'),
    path("create/<str:us>/",views.create,name='create'),
    path("join/<str:us>/",views.join,name='join'),
    path("deletejoin/<str:us>/",views.deletejoin,name='deletejoin'),

    path("register/", views.register, name='register'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
]