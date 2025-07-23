from django.urls import path

from . import admin
from .views.user import UserList, UserDetail
from .views.task import TaskList, TaskDetail

urlpatterns = [
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]