from django.shortcuts import render
from Blog.models import Post

def blog_view(request):
    posts = Post.objects.all()  # <-- این خط اضافه شود
    context = {'posts':posts}   # <-- این خط اضافه شود
    return render(request, 'Blog/blog.html', context)


def blog_single(request):
    return render(request,'Blog/blog-single.html')


def test(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'test.html',context)