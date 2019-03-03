from django.urls import path, re_path

from . import views

urlpatterns = [
    path('api/register_user', views.register_user, name='register_user'),
    path('register/<int:number>', views.sms_register, name='sms_register'),
    path('', views.sms_response, name='sms'),
]
