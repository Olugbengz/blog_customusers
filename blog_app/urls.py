from django.urls import path
from . import views
from .views import BlogPostListView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='home'),
    path('new_post/', views.add_post, name='new_post'),
    path('post_details/<int:pk>', views.display_post, name='post_details'),
    path('update_post/<int:pk>', views.update_post, name='update_post'),
]
