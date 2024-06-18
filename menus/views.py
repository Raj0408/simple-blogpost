from django.shortcuts import redirect, render ,get_object_or_404

from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse

from menus.models import blog

from .forms import blog_form as bl


def menu(request):
    blogs = blog.objects.all()
    doc = {'blogs':blogs , 'form' : bl.blogform()}
    context ={}
    formm = bl.blogform()
    if request.method == 'POST':
         formm = bl.blogform(request.POST)
         if formm.is_valid():
             print("form is valid")
             formm.save()
    return render(request,'menu_tmep/home.html',{'doc':doc})


def blog_post(request,id):
    blogs = blog.objects.get(id=id)
    return render(request,'menu_tmep/blog_post.html',{'blogs':blogs})


def blog_formm(request, id=0):
     return render(request,'menu_tmep/blog_form.html',{'form': formm})

def delete_blog(request, blog_id):
    blogs = blog.objects.get(id=blog_id)
    # blogs = get_object_or_404(blog, id=blog_id)
    if request.method == 'POST':
        blogs.delete()
        return redirect(reverse('menu'))
    
      # replace 'blog_list' with the name of your blog list view
    else:
        return redirect('')  # replace 'blog_detail' with the name of your blog detail view

def edit_blog(request, blog_id,form):
    blogs = get_object_or_404(blog, id=blog_id)
    if request.method == 'POST':
        form = bl.blogform(instance=blogs)  # replace 'BlogForm' with the name of your form class
        if form.is_valid():
            form.save()
            return redirect('blog', id=blogs.id)
        
    return redirect(reverse('blog', args=[blog_id,form]))