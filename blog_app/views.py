from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import AddNewPostForm
from users.models import CustomUser
from .models import BlogPost

# Create your views here.


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})


def add_post(request):
    context = {}
    form = AddNewPostForm(request.POST or None)   
    if form.is_valid():
        obj = form.save(commit=False)        
        if request.user.is_authenticated:            
            obj.save()
            return redirect('home')
        else:
            form.add_error(None, 'You must be logged in to add a post!')
    context['form'] = form
    return render(request, 'add_post.html', context)


def display_post(request, pk):
    if request.user.is_authenticated:
        this_post = BlogPost.objects.get(pk=pk)
        return render(request, 'display_post.html', {'this_post': this_post})
    else:
        messages.success(request, 'You need to login to view post details!')
        return redirect('home')


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




