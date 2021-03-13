from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name = 'detail'),  #add
    path('new/', views.new, name = 'new'),  #add
    path('create/', views.create, name = 'create'),    #add
    path('newblog/', views.blogpost, name = 'newblog'),  #add
    path('<int:blog_id>/delete', views.delete, name = 'delete'),    #add
    path('<int:blog_id>/edit', views.edit, name = 'edit'),  #add
]
