from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
	posts = Post.objects
	return render(request, 'blog/blog.html', {'posts' : posts})
