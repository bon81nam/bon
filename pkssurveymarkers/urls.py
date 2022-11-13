from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
#from django.conf.urls.defaults import patterns, include, url
from .views import map, front_login, points


urlpatterns = [
    path('map/', map, name='map'),
    path('', front_login, name='front_login'),
    path('logout/', LogoutView.as_view(next_page='front_login'), name='logout'),
    path('points/', points, name='points')
]
