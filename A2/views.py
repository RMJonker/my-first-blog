from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@login_required
def index(request):
	tasks = Task.objects.filter(important=False, owner=request.user).order_by('due_date')
	important_tasks = Task.objects.filter(important=True, owner=request.user).order_by('due_date')
	return render(request, 'A2/index.html', {'tasks': tasks, 'important_tasks': important_tasks})

def notloggedin(request):
	return render(request, 'A2/notloggedin.html')

def help(request):
	return render(request, 'A2/help.html')

@login_required
def addtask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('A2:index')
    else:
        form = TaskForm()
    return render(request, 'A2/task_edit.html', {'form': form})

@login_required
def edittask(request, task_id):
    task = Task.objects.get(pk=task_id)
    user_check = task.owner
    if user_check == request.user:
	    if request.method == "POST":
	        form = TaskForm(request.POST, instance=task)
	        if form.is_valid():
	            task = form.save()
	            return redirect('A2:index')
	    else:
	    	form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task)
    return render(request, 'A2/task_edit.html', {'form': form})

def removetask(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('A2:index')

def clearlist(request):
	task = Task.objects.filter(owner=request.user)
	if request.method == "POST":
		task.delete()
		return redirect('A2:index')


#Code underneath is for the REST API

@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """
    Retrieve, update or delete a task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)