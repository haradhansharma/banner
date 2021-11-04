from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Category),


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'user', 'created_at', 'updated_at' ]
    
    
# admin.site.register(Blog, BlogAdmin),
