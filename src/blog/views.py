from django.shortcuts import render

# from django.http import HttpResponse


# Create your views here:
def posts_list(request):
    # return HttpResponse('<h1>Hello, World from blog.views.py!</h1>')
    n = ['Oleg', 'Masha', 'Olja', 'Ksu']
    # return render(request, 'blog/base_blog.html', context={'names': n})
    return render(request, 'blog/index.html', context={'names': n})