from django.views.generic import DetailView, CreateView
from django.http.response import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.models import Accounts
from .models import Profiles
from .forms import ProfileForms

# Create your views here.
@method_decorator(
   decorator=[login_required,]
, name='get')
class ProfileView(DetailView):
   http_method_names = ['get']
   template_name = 'profiles/page.html'
   model = Accounts

   def dispatch(self, request, *args, **kwargs):
      if kwargs['pk'] != request.user.id:
         return HttpResponseNotFound()
      return super().dispatch(request, *args, **kwargs)

class CreateProfile(CreateView):
   http_method_names = ['get', 'post']
   template_name = 'profiles/profile_create.html'
   model = Profiles
   form_class = ProfileForms
   
   def get_success_url(self):
      return f'http://localhost:8000/profile/preview/{self.request.user.id}'
   
   def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      kwargs['user'] = self.request.user
      return kwargs