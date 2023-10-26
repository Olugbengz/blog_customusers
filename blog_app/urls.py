from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_post/', views.add_post, name='new_post'),
    path('update_post/<int:pk>', views.update_post, name='update_post'),
]
