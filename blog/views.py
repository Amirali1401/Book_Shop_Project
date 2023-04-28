from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , Http404

from .models import Blog
from .forms import BlogForm

# Create your views here

@login_required()
def read_view_blog(request):
    blogs = Blog.objects.order_by('date_created')
    return render(request , 'blog/list_views_blogs.html' , context={'blogs':blogs})


@login_required()
def detail_view_blog(request , blog_id):
    blog = get_object_or_404(Blog , id = blog_id)

    # except Blog.DoesNotExist:
    #     return Http404('Your detail Not Found')

    return render(request , 'blog/delete_view_blog.html' , context={'blogs':blog})


@login_required()
def write_view_blog(request):
    form = BlogForm( data=request.POST)
    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.author = request.user
        form_obj.save()
        return redirect('list_blogs')

    return render(request, 'blog/write_new_blog.html/', context={'form': form})


@login_required()
def delete_view_blog(request , blog_id):
    blog = get_object_or_404(Blog , id = blog_id)
    if blog:
        blog.delete()
        return HttpResponse('Your blog was deleted')

