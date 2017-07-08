from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'index/', views.index, name='detail'),
    url(r'^(?P<word_id>[0-9]+)/$', views.new_word, name='detail'),
    url(r'^(?P<word_id>[0-9]+)/results/$', views.results, name='results'),
]