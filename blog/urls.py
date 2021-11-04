from django.contrib import admin
from django.urls import path, include
from  blog.views import *
from froala_editor import views

app_name = 'blog'
urlpatterns = [
    path('froala_editor/',include('froala_editor.urls')),
    path('', home, name='home'),
    path('blog/<int:id>/', get_blog, name='get_blog'),
    
]