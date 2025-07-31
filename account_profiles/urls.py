from django.urls import path
from .views import ProfileView

app_name = 'account_profiles'
urlpatterns = [
   path('preview', view=ProfileView.as_view(), name='preview'),
]