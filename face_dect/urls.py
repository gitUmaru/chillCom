from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#indez url
    url(r'^info/$', views.info, name='info'),#result url
    url(r'^history/$', views.getHistory, name='history'),#history url
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^music_playlist', views.music_playlist, name='music_playlist')
]
