from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.contrib.auth import login
from .forms import RegisterForms, LoginForms

# Create your views here.
class RegisterView(CreateView):
   http_method_names = ['get', 'post']
   template_name = 'auth/register.html'
   form_class = RegisterForms
   success_url = '/authentication/login'

class UserLoginView(FormView):
   http_method_names = ['get', 'post']
   template_name = 'auth/login.html'
   form_class = LoginForms
   success_url = '/'

   def form_valid(self, form):
      login(self.request, user=form.valid_user)
      return super().form_valid(form)
   
   def get_success_url(self):
      next = self.request.GET.get('next', '/')
      return next