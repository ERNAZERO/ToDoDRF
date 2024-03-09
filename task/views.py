from rest_framework.generics import get_object_or_404
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status, permissions, generics


class GetListOfTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            todo = Task.objects.create(
                title=request.data['title'],
                description=request.data['description']
            )
            todo.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data, status=status.HTTP_200_OK)


class TaskCompleteView(APIView):
    def patch(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.completed = True
        task.save()

        return Response({"message": "Task completed successfully"}, status=status.HTTP_200_OK)


class DeleteTaskView(APIView):

    def delete(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        if task:
            task.delete()
            return Response({"Task has deleted!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "ERROR"}, status=status.HTTP_400_BAD_REQUEST)

