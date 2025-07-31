from django.urls import path, include
from .views import SubmissionView

app_name = 'permit_application'
urlpatterns = [
    path('submission', view=SubmissionView.as_view(), name='submission'),
]