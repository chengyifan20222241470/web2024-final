from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
import markdown


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.content = markdown.markdown(blog.content)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Blog.objects.create(title=title, content=content,
                            created_at=timezone.now())
        return redirect('blog_list')
    return render(request, 'blog/blog_create.html')
