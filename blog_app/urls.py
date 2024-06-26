from django.urls import path
from . import views
# from .views import BlogPostListView
# BlogPostCreateView

urlpatterns = [
    path('', views.home, name='home'),
    # path('new_post/', BlogPostCreateView.as_view(), name='new_post'),
    path('new_post/', views.add_post, name='new_post'),
    path('post_details/<int:pk>/', views.display_post, name='post_details'),
    path('update_post/<int:pk>/', views.update_post, name='update_post'),
    path('send_comment/<int:pk>/', views.send_comment, name='send_comment')
]
