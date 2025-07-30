from django.shortcuts import render

def landing_page(request):
   if request.method == 'GET':
      return render(request, template_name='landing/page.html')