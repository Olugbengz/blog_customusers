from django.urls import path
from . import views
from .views import RegForm

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', RegForm.as_view(), name='register'),
]
