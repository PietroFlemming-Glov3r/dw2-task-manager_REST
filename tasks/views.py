from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

    # Não sei se isso vai funcionar
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    from django.shortcuts import render

    def home(request):
        return render(request, "tasks/home.html")

    def login_view(request):
        return render(request, "tasks/login.html")

    def register_view(request):
        return render(request, "tasks/register.html")

    def tasks_view(request):
        tarefas = [{"nome": "Fazer compras"}, {"nome": "Estudar Django"}]  # Exemplo
        return render(request, "tasks/tasks.html", {"tarefas": tarefas})
