from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddNewPostForm
from users.models import CustomUser
from .models import BlogPost

# Create your views here.


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})


def add_post(request):
    form = AddNewPostForm(request.POST or None)
    # if request.user.is_authenticated:
    #     form = AddNewPostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            add_new_post = form.save(commit=False)
            add_new_post.save()
            return redirect('home')
    return render(request, 'add_post.html', {'form': form})


def display_post(request, pk):
    this_post = BlogPost.objects.get(pk=pk)
    return render(request, 'display_post.html', {'this_post': this_post})


def update_post(request, pk):
    # form = AddNewPostForm(request.POST or None)
    if request.user.is_authenticated:
        current_blog = get_object_or_404(BlogPost, pk=pk)
        # current_blog = BlogPost.objects.get(pk=pk)
        form = AddNewPostForm(request.POST or None, request.Files, instance=current_blog)
        if form.is_valid():
            form.save()
            redirect('home')
        return render(request, 'update_post.html', {'form': form})
    else:
        return redirect('home')




