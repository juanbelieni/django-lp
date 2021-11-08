from django.urls import path
import todo.views as todo_views

urlpatterns = [
    path('', todo_views.index),
    path('zapzap2/', todo_views.zapzap2),
    path('todo/', todo_views.todos),
    path('todo/<int:id>', todo_views.todo, name="todo-dinamico"),
    path('todo_2', todo_views.todo_2, name="todo-template"),
    path('animes/', todo_views.animes),
]
