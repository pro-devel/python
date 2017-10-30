from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'home/index.html', context)


def details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'details/index.html', {'post': post})



