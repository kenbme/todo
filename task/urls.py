from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("add-tasks/", views.add_tasks, name="add-tasks"),
    path("task-edit/<int:id>/", views.task_edit, name="task-edit"),
    path("delete_task/<int:id>/", views.delete_task, name="delete-task"),
]
