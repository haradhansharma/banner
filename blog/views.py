from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
    context = {}
    try:
        blogs = Blog.objects.all()
        context['all'] = blogs    
    except Exception as e:
        print(e)
    return render(request, 'blog/home.html', context)
    

def get_blog(request, id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id = id)
        context['blog'] = blog_obj        
    except Exception as e:
        print(e)        
    return render(request, 'blog/blog_details.html', context)
