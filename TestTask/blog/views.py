from .models import Blog,BlogAuthor
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

 
 
class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title','author','blog_text','blog_date']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')