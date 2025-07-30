from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
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
   
   def save(self, commit = True):
      instance = self.instance
      instance.set_password(self.cleaned_data['password'])
      return super().save(commit)

class LoginForms(AuthenticationForm):
   error_messages = {
      'invalid_login': _('Login gagal, periksa nama pengguna dan sandi anda!'),
   }