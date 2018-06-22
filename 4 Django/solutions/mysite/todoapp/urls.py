

from django.urls import path
from . import views


app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo')
]

