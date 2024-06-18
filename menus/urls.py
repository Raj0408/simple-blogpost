from django.urls import reverse , path , include
from . import views


urlpatterns = [
    path('',view=views.menu , name='menu'),
    path('blog_post/<int:id>/',view=views.blog_post , name='blog'),
    path('blog_formm/',view=views.blog_formm , name='blog_formmm'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),


]