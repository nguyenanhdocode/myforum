from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *

# Register your models here.

class PostFormAdmin(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostFormAdmin
    list_display = ('title', 'created', 'active', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
