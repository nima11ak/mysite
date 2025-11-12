from django.shortcuts import render,get_object_or_404
from Blog.models import Post


def blog_view(request):
    posts = Post.objects.all()  # <-- این خط اضافه شود
    context = {'posts':posts}   # <-- این خط اضافه شود
    return render(request, 'Blog/blog.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid)
    context = {'post': post, 'single': True}  
    return render(request, 'Blog/blog-single.html', context)


def test(request, pid):
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
