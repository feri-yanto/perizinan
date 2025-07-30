from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterForms

# Create your views here.
class RegisterView(CreateView):
   http_method_names = ['get', 'post']
   template_name = 'auth/register.html'
   form_class = RegisterForms
   success_url = '/authentication/login'