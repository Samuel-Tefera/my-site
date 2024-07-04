from django.shortcuts import render
from django.views.generic import ListView

from .models import Post, Comment, Like


# Create your views here.

class StartPageView(ListView):
    template_name = 'blog/blog-home.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-date']
    
    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data
    

class AllPostPageView(ListView):
    template_name = 'blog/all-post.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'