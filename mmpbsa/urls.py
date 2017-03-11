from django.conf.urls import url

from . import views

urlpatterns = [
    # the homepage of the mmpbsa application
    url(r'^$', views.index, name='mmpbsa'),
    # also the home page
    url(r'^index/', views.index, name='index'),
    # theory page about MMPBSA
    url(r'^theory/', views.theory, name = 'theory'),

    url(r'^result/', views.result, name='result'),

    url(r'^get_name/', views.get_name, name='get_name')
]
