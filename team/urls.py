from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.team, name='team'),
    url(r'^about', views.about, name='about'),
    url(r'^jesus', views.chuy, name='jesus'),
    url(r'^greg', views.greg, name='greg'),
    url(r'^yu', views.yu, name='yu'),
    url(r'^lance', views.lance, name='lance'),
]
