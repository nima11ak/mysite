from django.shortcuts import render,get_object_or_404
from Blog.models import Post
from django.utils import timezone 
from django.db.models import F


def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now,status=True).order_by('-published_date')
    context = {'posts':posts}
    return render(request, 'Blog/blog.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid)
    post.counted_views = F('counted_views') + 1
    post.save()
    post.refresh_from_db()
    context = {'post': post, 'single': True}  
    return render(request, 'blog-single.html', context)

def test(request, pid):
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
