from django.shortcuts import get_object_or_404, render
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'blog/index.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', { 'post': post })


