from django.urls import re_path

from MyGIS import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^map/$', views.maps, name='map'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^articles/(?P<article_id>[0-9]+)/$', views.show_articles, name='article'),
]
