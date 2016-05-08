from django.conf.urls import url
from django.contrib import admin

from vkapi import views

urlpatterns = [
    url(r'^token(?P<code>.+)/$', views.get_token),
    url(r'fFriends/(?P<token>.+)',views.getFriends),

]