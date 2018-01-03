from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^(?P<thread_id>[0-9]+)/$', views.thread_page, name='thread_page'),
]