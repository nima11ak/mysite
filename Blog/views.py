from django.shortcuts import render


def blog_view(request):
    return render(request,'Blog/blog.html')


def blog_single(request):
    return render(request,'Blog/blog-single.html')

