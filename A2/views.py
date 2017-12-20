from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Task

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