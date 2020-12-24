from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ["user"]
    
    def get_absolute_url(self):
        return reverse("blogs_by_author", args=[str(self.id)])
    
    def __str__(self):
        return self.user.username

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    blog_text = models.TextField(max_length=3000, help_text='Введите сюда текст вашего поста')
    blog_date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-blog_date"]
    
    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.id)])

    def __str__(self):
        return self.title

#class BlogSubscription(models.Model):
#    subscription = models.ForeignKey(Blog,on_delete=models.SET_NULL, null=True)
    
