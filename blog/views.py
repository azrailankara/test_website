from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories
    })

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category)
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'current_category': category
    })

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
        created_date__year=year,
        created_date__month=month,
        created_date__day=day,
        slug=slug
    )
    categories = Category.objects.all()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'categories': categories
    })
