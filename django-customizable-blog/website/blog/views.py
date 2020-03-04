# from django.shortcuts import render
from django.views import generic
from .mdoels import Post

class PostList(generic.ListView):
    # Only show posts with a status=1, i.e. published
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.Detailview):
    model = Post
    template_name = 'post_detail.html'
