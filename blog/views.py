# blog/views.py
from django.views.generic import ListView, DetailView
from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'anything_you_want'
    """[summary]
    В этом новом представлении мы определяем модель, которую мы используем, Post и 
шаблон, с которым мы хотим ее связать, post_detail.html. По умолчанию DetailView 
предоставит контекстный объект, который мы можем использовать в нашем шаблоне, 
называемый либо объектом, либо строчным именем нашей модели post. Кроме того, 
DetailView ожидает либо первичный ключ, либо slug, переданный ему в качестве 
идентификатора. Подробнее об этом вкратце.
    """
