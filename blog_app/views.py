from django.shortcuts import render, redirect
from .forms import AddNewPostForm
from users.models import CustomUser
from .models import BlogPost

# Create your views here.


def home(request):
    posts = BlogPost.objects.all()
    return render(request, '../../users/templates/base.html', {posts: posts})


def add_post(request):
    form = AddNewPostForm(request.POST or None)
    # if request.user.is_authenticated:
    #     form = AddNewPostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            add_post = form.save()
            return redirect('home')
    return render(request, 'add_post.html', {'form': form})

