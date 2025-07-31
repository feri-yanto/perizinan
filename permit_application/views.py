from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(
   decorator=[login_required,]
, name='dispatch')
class SubmissionView(TemplateView):
   http_method_names = ['get']
   template_name = 'permit/permit.html'