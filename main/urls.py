from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/', views.all_news),
    url(r'^cards/', views.all_cards),
    url(r'^training/', views.training),
    ]