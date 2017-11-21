from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Post,Banner

# Create your views here.

def index(request):
    all_Posts = Post.objects.all()
    all_Banners = Banner.objects.all()
    context = {
        "all_Posts": all_Posts,
        "all_Banners": all_Banners

    }
    return render(request, "index.html", context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', context={'post': post})

def bannner_detail(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    return render(request, 'banner.html', context={'banner': banner})