from django.shortcuts import render, redirect
from .models import Blog, Post
from .forms import PostForm



def index(request):
    """Главная страница."""
    posts = Post.objects.order_by('-date_added')[:5]
    context = {'posts': posts}
    return render(request, "blogs/index.html", context)

def new_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = PostForm()

    return render(request, 'blogs/new_post.html', {'form': form})
