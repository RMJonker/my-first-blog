from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
	tasks = Task.objects.filter(important=False).order_by('due_date')
	important_tasks = Task.objects.filter(important=True).order_by('due_date')
	return render(request, 'A2/index.html', {'tasks': tasks, 'important_tasks': important_tasks})

def help(request):
	return render(request, 'A2/help.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'A2/post_list.html', {'posts': posts})

def addtask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'A2/task_edit.html', {'form': form})

def edittask(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'A2/task_edit.html', {'form': form})