from django.urls import path
from . import views

urlpatterns = [
    path(r'^signup/$', views.signup, name = 'signup'),     #add
    path(r'^login/$', views.login, name = 'login'),        #add
    path(r'^logout/$', views.logout, name = 'logout'),     #add
]