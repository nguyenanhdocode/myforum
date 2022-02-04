from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.text import slugify

from .models import *
from .forms import *

# Create your views here.

def home(request, category=None):

    posts = Post.objects.filter(active=True)

    if category:
        posts = posts.filter(category=category)

    return render(request, 'baseapp/home.html', {
        'posts': posts,
    })


def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(cd['title'])
            new_post.save()
            return HttpResponseRedirect(reverse('baseapp:home'))
    else:
        form = PostForm()

    return render(request, 'baseapp/post_create.html', {
        'form': form,
    })


def detail_post(request, slug):

    post = Post.objects.get(slug=slug)

    return render(request, 'baseapp/post_detail.html', {
        'post': post,
    })


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('baseapp:detail', args=(post.slug, )))
    else:
        form = PostForm(instance=post)

    return render(request, 'baseapp/post_edit.html', {
        'form': form,
    })


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('baseapp:home'))
    
    return render(request, 'baseapp/post_delete.html', {
        'post': post,
    })
