from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT

from froala_editor.fields import FroalaField

class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, blank=False)
    
    def __str__(self) -> str:
        return self.category_name
    
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    banner_image = models.ImageField(upload_to ="blog_banner")
    content = FroalaField()
    category = models.ForeignKey(Category, on_delete = models.SET_DEFAULT, default='Category Removed')#On category delete default category
    user = models.ForeignKey(User, on_delete=models.CASCADE)#On user Delete , delete the blog
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
    
    def __str__(self):
                       
        return self.title
