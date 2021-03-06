"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from data_app import views as data_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, {'next_page': '/'}, name="logout"),
    url(r'^registration/', data_views.registration, name="registration"),
    url(r'^$', data_views.home, name="home"),
    url(r'^movies/$', data_views.movie_list, name="movie_list"),
    url(r'^movies/(?P<movie_id>\d+)/$', data_views.movie_detail),
    url(r'^movies/([0-9]+)/(?P<user_id>\d+)/$', data_views.user_detail),
    url(r'^users/$', data_views.user_list),
    url(r'^users/(?P<user_id>[0-9]+)/$', data_views.user_detail),
    url(r'^users/([0-9]+)/(?P<movie_id>\d+)/$', data_views.movie_detail),
]
