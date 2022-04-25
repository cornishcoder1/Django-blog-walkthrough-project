from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content') # Tells Django we want to use Summernote for the Content field in Post class. 
