from django.shortcuts import render,get_object_or_404

from blog.models import post


# Create your views here.


def render_post(request):
    posts = post.objects.all()
    return render(request, 'post.html', {'posts': posts})


def post_detail(request, post_id):
    poster= get_object_or_404(post, pk=post_id)
    return render(request, 'post_detail.html', {'post': poster})
