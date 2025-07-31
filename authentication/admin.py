from django.contrib import admin
from .models import Accounts, ProfileModels

# Register your models here.
admin.site.register(model_or_iterable=[Accounts, ProfileModels])