from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def post_detail(request, pk):
    post = Post.objects.filter(pk=pk)
    if len(post) == 0:
        return render(request, 'blog/404.html', {})	
    return render(request, 'blog/post_detail.html', {'post': post[0]})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})