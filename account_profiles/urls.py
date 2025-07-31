from django.urls import path
from .views import ProfileView, CreateProfile

app_name = 'account_profiles'
urlpatterns = [
   path('preview/<int:pk>', view=ProfileView.as_view(), name='preview'),
   path('create', view=CreateProfile.as_view(), name='create'),
]