from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .views import RegisterView, UserLoginView

app_name = 'authentication'
urlpatterns = [
   path('register', view=RegisterView.as_view(), name='register'),
   path('login', view=UserLoginView.as_view(), name='login'),
   path('logout', view=login_required(function=LogoutView.as_view(), login_url='/authentication/login'), name='logout'),
]