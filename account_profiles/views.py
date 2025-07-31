from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(
   decorator=[login_required,]
, name='get')
class ProfileView(TemplateView):
   http_method_names = ['get']
   template_name = 'profiles/page.html'