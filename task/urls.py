from django.urls import path
from .views import (CreateTaskView,
                    GetListOfTask,
                    TaskDetailView,
                    TaskCompleteView,
                    DeleteTaskView
                    )


urlpatterns = [
    path('task_list/', GetListOfTask.as_view(), name='see-list-of-task'),
    path('<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
    path('create_task/', CreateTaskView.as_view(), name='create-task'),
    path('<int:task_id>/update_task/', TaskCompleteView.as_view(), name='complete-task'),
    path('<int:task_id>/delete_task/', DeleteTaskView.as_view(), name='delete-task'),
]
