from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,BlogAuthor
from django.views.generic import ListView

 
 
class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'