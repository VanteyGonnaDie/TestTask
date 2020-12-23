from django.urls import path
 
from .views import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView
 
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new', BlogCreateView.as_view(), name='blog_new' ),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete')
]