from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#indez url
    url(r'^info/$', views.info, name='info'),#result url
    url(r'^history/$', views.getHistory, name='history'),#history url
    url(r'^chat/$', views.chat, name='chat'),
<<<<<<< HEAD
    url(r'^animation/$', views.animation, name='animation'),
    url(r'^main/$', views.main, name='main'),
    url(r'^option/$', views.option, name='option'),
    url(r'^welcome/$', views.welcome, name='welcome'),
=======
    url(r'^music_playlist', views.music_playlist, name='music_playlist')
>>>>>>> dd0eaca4d1ca1ba3eb5391f0d8aa283881f9c72c
]
