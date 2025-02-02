from django.urls import path
from .views import TaskViewSet

urlpatterns = [
    path("", TaskViewSet.home, name="home"),
    path("tasks/", TaskViewSet.tasks_view, name="tasks"),
]
