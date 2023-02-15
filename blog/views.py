from django.shortcuts import render

# Create your views here.


def blog_views(request):
    return render(request, "blog/blog.html")


def single_views(request):
    return render(request, "blog/blog-single.html")
