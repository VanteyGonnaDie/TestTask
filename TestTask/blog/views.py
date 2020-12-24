from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

 
 
class BlogListView(ListView):       #Список всех постов
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):   #Подробный просмотр поста
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):   #Создание поста
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title','author','blog_text','blog_date']

class BlogDeleteView(DeleteView):   #Удаление поста
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')

class BloggersList(ListView):       #Лист всех авторов
    model = BlogAuthor
    template_name = 'bloggers.html'

class BlogsByAuthor(ListView):      #Просмотр постов выбранного автора
    model = Blog
    template_name = 'blogs_by_author.html'
    def get_queryset(self):
        id =self.kwargs['pk']
        target = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=target)

class MyBlog(ListView):             #Просмотр своих постов
    model = Blog,BlogAuthor
    template_name = 'blogs_by_user.html'
    def get_queryset(self):
        id = self.kwargs['pk']
        target = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=target)

class MySubscription(ListView):     #Подписки не реализованны
    model = Blog
    template_name = 'user_subscription.html'
    def SubList(self):
        sub_list = []

