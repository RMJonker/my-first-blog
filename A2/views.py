from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'A2/index.html')

def help(request):
	return render(request, 'A2/help.html')

"""def post_list(request):
    return render(request, 'A2/post_list.html')"""