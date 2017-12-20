from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
	return render(request, 'A2/index.html')

def help(request):
	return render(request, 'A2/help.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'A2/post_list.html', {})