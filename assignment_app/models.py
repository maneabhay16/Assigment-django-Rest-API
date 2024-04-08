import random
import string
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify


class Category(models.Model):
    category_name = models.CharField()
    
    def __str__(self):
        return self.category_name
    
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=60)
    body = models.TextField(max_length=300)
    pdf = models.FileField(upload_to='blog_pdfs/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")  
    post_date = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title + "" + self.author.username + "" + self.category.category_name)
            self.slug = base_slug + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        return super().save(*args, **kwargs)

