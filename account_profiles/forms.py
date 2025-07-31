from django import forms
from .models import Profiles

class ProfileForms(forms.ModelForm):
   class Meta:
      model = Profiles
      fields = '__all__'
      widgets = {
         'account': forms.Select(attrs={
            'disabled': True,
         }),
         'date_of_birth': forms.DateInput(attrs={
            'type': 'date',
         }),
      }