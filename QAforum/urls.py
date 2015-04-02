from django.conf.urls import patterns, include, url
from django.conf import settings

from QAforum import views

urlpatterns = patterns('',
	url(r'^register/', views.register,name='reg' ),
	url(r'^login/', views.login,name='login' ),
	url(r'^question/', views.question),
	url(r'^home/', views.home,name='home' ),
	url(r'^qaform/', views.display,name='post' ),
        url(r'^ansform/(?P<ques_id>\d+)/', views.writeans),
        url(r'^answer/(?P<ques_id>\d+)/', views.answer),
	

	)
