from django.urls import path
from . import views
urlpatterns = [
    path("",views.main,name='main'),
    path("home",views.home,name='home'),
    path("create",views.create,name='create'),
    path("join/<str:us>/",views.join,name='join'),
]