from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("add-task/", views.add_task, name="add-task"),
    path("edit-task/<int:pk>/", views.edit_task, name="edit-task"),
    path("delete-task/<int:pk>/", views.delete_task, name="delete-task"),
]
