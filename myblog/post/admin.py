from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')
admin.site.register(Post, PostAdmin)
