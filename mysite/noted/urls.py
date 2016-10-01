from django.conf.urls import url
from . import views

app_name = 'noted'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<file_id>[0-9]+)/$', views.detail, name='detail'),
]