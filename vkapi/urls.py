from django.conf.urls import url
from django.contrib import admin

from vkapi import views

urlpatterns = [
    url(r'^token$', views.get_token),
    url(r'^msg$', views.send_message),
    url(r'fFriends',views.getFriends),
]