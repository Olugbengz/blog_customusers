from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib import messages
from .forms import AddNewPostForm
from users.models import CustomUser
from .models import BlogPost

# Create your views here.

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'home.html'  # Replace with the actual template name
    context_object_name = 'posts' 
# def home(request):
#     posts = BlogPost.objects.all()
#     # UserModel = get_user_model()
#     # author = UserModel.objects.all()


#     return render(request, 'home.html', {'posts': posts})


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
    this_post = BlogPost.objects.get(pk=pk)
    return render(request, 'display_post.html', {'this_post': this_post})
    


def update_post(request, pk):
    # form = AddNewPostForm(request.POST or None)
    if request.user.is_authenticated:
        current_blog = get_object_or_404(BlogPost, pk=pk)
        # current_blog = BlogPost.objects.get(pk=pk)
        form = AddNewPostForm(request.POST or None, request.Files, instance=current_blog)
        if form.is_valid():
            current_blog = form.save()
            current_blog.save()
            redirect('home')
        return render(request, 'update_post.html', {'form': form})
    else:
        return redirect('home')




