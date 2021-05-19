# from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


# Create your views here:
def posts_list(request):
    # return HttpResponse('<h1>Hello, World from blog.views.py!</h1>')
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
    
    
def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})