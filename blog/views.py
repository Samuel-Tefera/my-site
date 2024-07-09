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
    def is_stored(self,request, post):
        stored_post = request.session.get('stored-post')
        if stored_post == None or len(stored_post) == 0:
            return False
        return post in stored_post
    
    def get(self, request, slug):
        post= Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post.id)
        form = CommentForm
        
        return render(request, 'blog/post-detail.html', {
            'post' : post,
            'comments':comments,
            'form' : form,
            'saved_for_later' : self.is_stored(request, int(post.id))
        })
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post.id)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        
            return HttpResponseRedirect(reverse('post-detail', args=[slug]))
        
        context = {
            'post' : post,
            'comments':comments,
            'form' : comment_form,
            'saved_for_later' : self.is_stored(request, int(post.id))
        }
        
        return render(request, 'blog/post-detail.html', context)
    
    
class StoredPostView(View):
    def get(self, request):
        stored_posts = request.session.get('stored-post')
        context = {}
        
        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_post'] = False
        else:
            context['stored_posts'] = Post.objects.filter(id__in=stored_posts)
            context['has_post'] = True
        
        return render(request, 'blog/stored-post.html', context)
    
    def post(self, request):
        stored_posts = request.session.get('stored-post')
        
        if stored_posts == None or len(stored_posts) == 0:
            stored_posts = []
        
        post_id = int(request.POST.get('post-id'))
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session['stored-post'] = stored_posts
        
        detail_page = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(detail_page)