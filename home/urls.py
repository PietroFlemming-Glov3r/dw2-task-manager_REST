from django.urls import path
from . import views
from tasks.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('your-tasks/', views.tasks, name='your-tasks'),
    path('your-tasks/create/', TaskCreate.as_view(), name='create-task'),
]