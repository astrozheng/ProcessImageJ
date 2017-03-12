from django.conf.urls import url

from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    # the homepage of the mmpbsa application
    url(r'^$', index, name='index'),
    # also the home page
    url(r'^index/', index, name='index'),
    url(r'^parameters', index, name='index'),
    # theory page about MMPBSA
    url(r'^theory/', theory, name='theory'),

    url(r'^result/', result, name='result'),

    url(r'^get_name/', get_name, name='get_name'),
    url(r'^welcome', get_name, name='get_name'),
    #url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    # login window
    #url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    url(r'^login/', login, name = 'login'),
    url(r'^loggedin/', login, name = 'login'),
    url(r'^upload/', upload, name='upload')
]
