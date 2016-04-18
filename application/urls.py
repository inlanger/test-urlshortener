from django.conf.urls import url

from application import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<key>\w+)/$', views.link, name="link"),
    url(r'^!(?P<key>\w+)/$', views.settings, name="settings"),
]