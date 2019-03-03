from django.urls import path, re_path

from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path('api/register_user', views.register_user, name='register_user'),
    path('sms', views.sms_response, name='sms'),
]
