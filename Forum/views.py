from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')[:3]  # Get the latest 5 posts
    return render(request, 'Forum/home.html', {'posts': posts})

def publications(request):
    posts = Post.objects.all()
    return render(request, 'Forum/publications.html', {'posts': posts})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Forum/post_details.html', {'post': post})