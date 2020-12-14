from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo, name = 'todo'),
    path('todo_list', views.todo, name = 'todo'),
    path('task_list', views.task_list, name = 'task_list'),
    path('delete_todo/<int:task_id>', views.delete_todo, name = 'delete_todo'),
    # path('edit_todo/<int:task_id>', views.edit_todo, name = 'edit_todo'),
    path('show_todo', views.show_todo, name = 'show_todo')
]