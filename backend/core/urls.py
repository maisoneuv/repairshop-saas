from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home_view, name="home"),
    path('login', LoginView.as_view(), name='login'),
]