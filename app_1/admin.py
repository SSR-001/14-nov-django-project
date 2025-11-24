from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('slug', 'title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)

# class MyModelAdmin(SummernoteModelAdmin):

