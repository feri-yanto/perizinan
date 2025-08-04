from django import forms
from .models import Profiles

class ProfileForms(forms.ModelForm):
   class Meta:
      model = Profiles
      fields = '__all__'
      exclude = ['account',]
      widgets = {
         'date_of_birth': forms.DateInput(attrs={
            'type': 'date',
         }),
      }
   
   def __init__(self, user, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.user = user
   
   def save(self, commit = False):
      instance = super().save(commit)
      instance.account = self.user
      instance.save()
      return instance