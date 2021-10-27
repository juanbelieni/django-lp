from django.urls import path
import todo.views as todo_views

urlpatterns = [
    path('', todo_views.index),
]
