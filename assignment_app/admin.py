from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'summary', 'body', 'pdf', 'post_date', 'is_public')
    list_display_links = ('id','title')
    search_fields = ('title' , 'body' , 'summary')
    list_per_page = 10
    list_editable = ("is_public",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)