from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer
from django.core.paginator import Paginator

def home(request):
    return render(request, 'tasks/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('your-tasks')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        
    return render(request, 'registration/register.html')

@api_view(['GET'])
def api_tasks(request):
    if request.user.is_authenticated:
        user_tasks = Task.objects.filter(owner=request.user)
        name = request.query_params.get('name', None)
        tags = request.query_params.get('tags', None)
        ordering = request.query_params.get('ordering', None)

        if name:
            user_tasks = user_tasks.filter(name__icontains=name)
        if tags:
            user_tasks = user_tasks.filter(tags=tags)
        if ordering:
            user_tasks = user_tasks.order_by(ordering)

        serializer = TaskSerializer(user_tasks, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Unauthorized'}, status=401)
    
def tasks(request):
    if request.user.is_authenticated:
        user_tasks = Task.objects.filter(owner=request.user)
        name = request.GET.get('name', None)
        tags = request.GET.get('tags', None)
        ordering = request.GET.get('ordering', None)

        if name:
            user_tasks = user_tasks.filter(name__icontains=name)
        if tags:
            user_tasks = user_tasks.filter(tags=tags)
        if ordering:
            user_tasks = user_tasks.order_by(ordering)

        paginator = Paginator(user_tasks, 6)  # Limite de 6 itens por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'tasks/tasks.html', {
            'tarefas': page_obj,
            'query_params': request.GET
        })
    else:
        return redirect('login')
