from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import AddNewPostForm, CommentForm
from users.models import CustomUser
from .models import BlogPost, Blog, Category, Comment
from django.urls import reverse_lazy



def home(request):
    blog_cat = Blog.objects.filter()
    posts = BlogPost.objects.filter(blog_id=3).order_by('-created_at')
    dev_post = BlogPost.objects.filter(blog_id=1).order_by('-created_at')
    paginator = Paginator(posts, 4)
    dev_p_paginator = Paginator(dev_post, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dev_p_page_number = request.GET.get('page')
    dev_p_page_obj = dev_p_paginator.get_page(dev_p_page_number)

    return render(request, 'home.html', {'page_obj': page_obj, 'dev_p_page_obj': dev_p_page_obj, 'blog_cat': blog_cat})

# class BlogPostListView(ListView):
#     model = BlogPost
#     template_name = 'home.html'  # Replace with the actual template name
#     context_object_name = 'posts' 

@login_required(login_url='login')
def add_post(request):
    # if request.user.is_authenticated:       
    
    if request.method == 'POST':
        form = AddNewPostForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()            
            return redirect('home')
        else:
            form.add_error(None, 'You must be logged in to add a post!')
            form = AddNewPostForm(request.POST or None)
            return render(request, 'add_post.html', {'form': form})
    form = AddNewPostForm()        
    return render(request, 'add_post.html', {'form': form})


# @login_required(login_url='login')
def display_post(request, pk):    
    this_post = BlogPost.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'this_post': this_post,
        'comment_form': comment_form
    }
    
    return render(request, 'display_post.html', context)

    

@login_required(login_url='login')
def update_post(request, pk):
    # form = AddNewPostForm(request.POST or None)
    if request.user.is_authenticated:
        current_blog = get_object_or_404(BlogPost, pk=pk)
        # current_blog = BlogPost.objects.get(pk=pk)
        form = AddNewPostForm(request.POST or None, instance=current_blog)
        if form.is_valid():
            current_blog = form.save()
            current_blog.save()
            return redirect('home')
    return render(request, 'update_post.html', {'form': form})


def delete_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(BlogPost, id=pk)
        post.delete()
        messages.success(request, messages.INFO, 'This blog post has been deleted successfully!')
        return redirect('home')
    else:
        messages.success(request, "Only an admin can delete this blog post!")
        return redirect('home')


def send_comment(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.comment_author = request.user            
            comment.save()
    return redirect('post_details', post.id)


def delete_comment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=pk)
        comment.delete()
       
        return redirect('home')
    
    return render(request, delete_comment.html, {'comment': comment})
    
    




    # function-based view 
# def home(request):
#     posts = BlogPost.objects.all()
#     # UserModel = get_user_model()
#     # author = UserModel.objects.all()


#     return render(request, 'home.html', {'posts': posts})

# class BlogPostCreateView(CreateView):
#     model = BlogPost
#     fields = ['blog', 'title', 'description', 'body', 'author', 'image']
#     success_url = reverse_lazy('home')




