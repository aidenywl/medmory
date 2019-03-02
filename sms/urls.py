from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.sms_response, name='sms')
]
