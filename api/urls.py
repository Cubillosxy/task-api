from django.urls import path

from api.views import TaskList
from api.views import TaskDetail

app_name = 'api'

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]

