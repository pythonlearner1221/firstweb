from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name','created_time','text']


admin.site.register(Comment,CommentAdmin)