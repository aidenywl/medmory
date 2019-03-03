from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('api/register_user', views.register_user, name='register_user'),
    path('task/test_scheduling/<slug:message>',
         views.test_scheduling, name='test_scheduling'),
    path('sms', views.sms_response, name='sms'),
	url(r'^', views.FrontendAppView.as_view()),
]
