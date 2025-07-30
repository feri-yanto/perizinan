from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import RegisterView
from .forms import LoginForms

app_name = 'authentication'
urlpatterns = [
   path('register', view=RegisterView.as_view(), name='register'),
   path('login', view=LoginView.as_view(
      template_name='auth/login.html',
      form_class=LoginForms,
   ), name='login'),
   path('logout', view=login_required(function=LogoutView.as_view(), login_url='/authentication/login'), name='logout'),
]