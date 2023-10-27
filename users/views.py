from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login_user.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'logout_user.html')


class RegForm(View):
    form_class = CustomUserCreationForm
    initial = {'key': 'value'}
    template_name = 'register_user.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

# Work on this later!
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        UserModel = get_user_model()
        if form.is_valid():
            if UserModel.objects.filter(email='email').first():
                messages.success(request, "User already exit, register or login with your credentials!")
                return render(request, self.template_name)
            else:
                form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})





