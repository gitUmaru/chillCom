from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#indez url
    url(r'^info/$', views.info, name='info'),#result url
    url(r'^history/$', views.getHistory, name='history'),#history url
    url(r'^chat/$', views.chat, name='chat'),
<<<<<<< HEAD

=======
>>>>>>> 2428b2626c2d97fe7c88b0b3032654be57a8ac3e
    url(r'^animation/$', views.animation, name='animation'),
    url(r'^main/$', views.main, name='main'),
    url(r'^option/$', views.option, name='option'),
    url(r'^welcome/$', views.welcome, name='welcome'),
<<<<<<< HEAD

    url(r'^music_playlist', views.music_playlist, name='music_playlist')

=======
    url(r'^music_playlist', views.music_playlist, name='music_playlist')
>>>>>>> 2428b2626c2d97fe7c88b0b3032654be57a8ac3e
]
