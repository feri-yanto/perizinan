from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Accounts

class RegisterForms(forms.ModelForm):
   password = forms.CharField(min_length=8, required=True, validators=[
      RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', message=['Sandi harus terdapat huruf kecil, kapital, angka dan simbol (@$!%*?&)']),
   ], widget=forms.PasswordInput())
   class Meta:
      model = Accounts
      fields = ['username', 'email', 'password']
      error_messages = {
         'username': {
            'unique': _('Nama Pengguna telah digunakan')
         },
         'email': {
            'unique': _('Email tersebut telah digunakan'),
         },
      }
   
   def save(self, commit = False):
      instance = super().save(commit)
      instance.set_password(self.cleaned_data['password'])
      instance.save()

class LoginForms(forms.Form):
   username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
   password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput())

   def __init__(self, request=None, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.request = request
      self.valid_user = None
   
   def clean(self):
      cleaned_data = super().clean()
      user = authenticate(self.request, **cleaned_data)
      if user is None:
         raise ValidationError(message='Login gagal, periksa nama pengguna dan sandi anda!', code='login_invalid')
      if user.is_active:
         self.valid_user = user
      else:
         raise ValidationError(message='Akun anda belum aktif', code='inactive')

      return cleaned_data