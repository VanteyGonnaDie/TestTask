from django.urls import path
 
from .views import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView, BloggersList, BlogsByAuthor
 
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new', BlogCreateView.as_view(), name='blog_new' ),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('bloggers/', BloggersList.as_view(), name='bloggers'),
    path('bloggers/<int:pk>/', BlogsByAuthor.as_view(), name='blogs_by_author')
]