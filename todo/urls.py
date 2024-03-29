from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("saveTodo", views.saveTodo, name="saveTodo"),
    path("removeTodo/<int:id>", views.removeTodo, name="removeTodo"),
    path("updateTodo/<int:id>", views.updateTodo, name="updateTodo"),
    path("search", views.search, name="search"),
]