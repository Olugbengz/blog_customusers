from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import AddNewPostForm
from users.models import CustomUser
from .models import BlogPost
from django.urls import reverse_lazy



def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})

# class BlogPostListView(ListView):
#     model = BlogPost
#     template_name = 'home.html'  # Replace with the actual template name
#     context_object_name = 'posts' 

@login_required(login_url='login')
def add_post(request):
    # if request.user.is_authenticated:       
    form = AddNewPostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()            
            return redirect('home')
        else:
            form.add_error(None, 'You must be logged in to add a post!')        
    return render(request, 'add_post.html', {'form': form})


# @login_required(login_url='login')
def display_post(request, pk):    
    this_post = BlogPost.objects.get(pk=pk)
    return render(request, 'display_post.html', {'this_post': this_post})
    

@login_required(login_url='login')
def update_post(request, pk):
    # form = AddNewPostForm(request.POST or None)
    if request.user.is_authenticated:
        current_blog = get_object_or_404(BlogPost, pk=pk)
        # current_blog = BlogPost.objects.get(pk=pk)
        form = AddNewPostForm(request.POST or None, request.FILES, instance=current_blog)
        if form.is_valid():
            current_blog = form.save()
            current_blog.save()
            return redirect('home')
    return render(request, 'update_post.html', {'form': form})
    
    




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




