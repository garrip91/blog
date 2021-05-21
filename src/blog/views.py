# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, Tag

from django.views.generic import View

from .utils import ObjectDetailMixin


# Create your views here:
def posts_list(request):
    # return HttpResponse('<h1>Hello, World from blog.views.py!</h1>')
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
    
    
class PostDetail(ObjectDetailMixin, View):
    # def get(self, request, slug):
        # post = get_object_or_404(Post, slug__iexact=slug)
        # return render(request, 'blog/post_detail.html', context={'post': post})
    model = Post
    template = 'blog/post_detail.html'
    
    
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
    
    
class TagDetail(ObjectDetailMixin, View):
    # def get(self, request, slug):
        # tag = get_object_or_404(Tag, slug__iexact=slug)
        # return render(request, 'blog/tag_detail.html', context={'tag': tag})
    model = Tag
    template = 'blog/tag_detail.html'