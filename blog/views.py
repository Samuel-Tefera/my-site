from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm


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


class PostDetailPage(View):
    def get(self, request, slug):
        post= Post.objects.get(slug=slug)
        form = CommentForm
        return render(request, 'blog/post-detail.html', {
            'post' : post,
            'form' : form
        })
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        
            return HttpResponseRedirect(reverse('post-detail', args=[slug]))
        
        context = {
            'post' : post,
            'form' : comment_form
        }
        
        return render(request, 'blog/post-detail.html', context)