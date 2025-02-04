import logging
from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from .models import Task
from .permissions import IsAuthor
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('id')  # Add default ordering
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']
    filterset_fields = ['tags']

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        tags = self.request.query_params.get('tags', None)
        ordering = self.request.query_params.get('ordering', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if tags:
            queryset = queryset.filter(tags=tags)
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Task.objects.all()
   serializer_class = TaskSerializer

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(done=self.request.data.get('done', serializer.instance.done))

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)