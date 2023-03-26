from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import BlogForm

# Create your views here

@login_required()
def read_view_blog(request):
    blogs = Blog.objects.order_by('date_created')
    return render(request , 'blog/list_views_blogs.html' , context={'blogs':blogs})



@login_required()
def write_view_blog(request):
     form = BlogForm( request.POST , instance=Blog)
     if form.is_valid():
         form_obj = form.save(commit=False)
         form_obj.user = request.user
         form_obj.save()

     return render(request , 'blog/write_new_blog/' , context={'form' : form})

