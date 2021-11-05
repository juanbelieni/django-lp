from django.urls import path
import todo.views as todo_views

urlpatterns = [
    path('', todo_views.index),
    path('zapzap2/', todo_views.zapzap2),
    path('todo/', todo_views.todos),
    path('todo/<int:id>', todo_views.todo, name="todo-dinamico")
]
