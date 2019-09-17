from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('complete/<id>', views.completeTodo, name="complete"),
    path('deletecompleted/', views.deleteCompleted, name="deletecomplete"),
    path('deleteall/', views.deleteAll, name="deleteall"),
]