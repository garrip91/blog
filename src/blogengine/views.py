from django.http import HttpResponse


def hello(request):
    # print()
    # print(request)
    # print()
    # print(dir(request))
    # print()
    # pass
    return HttpResponse('<h1>Hello, World!</h1>')