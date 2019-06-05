from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('todo/view/(?P<id>\d+)', views.details, name='views'),
    url('todo/delete/(?P<id>\d+)', views.delete, name='delete'),
    url(r'^todo/add$', views.add, name='add'),
    url('todo/add_todo', views.add_todo, name='add_todo'),
    url('todo/edit_todo/(?P<id>\d+)', views.edit_todo, name='edit_todo'),
    url('todo/update/(?P<id>\d+)', views.update, name='update'),
]
