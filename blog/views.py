from django.shortcuts import render

# Create your views here.

def start_page(request):
    return render(request, 'blog/blog-home.html')

def all_post_page(request):
    return render(request, 'blog/all-post.html')