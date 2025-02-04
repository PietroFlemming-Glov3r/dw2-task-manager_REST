from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

app_name = 'tasks'

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]