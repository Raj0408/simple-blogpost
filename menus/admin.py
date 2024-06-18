from django.contrib import admin

from menus.models import blog

# Register your models here.
admin.site.register(blog)   # This line registers the blog model with the admin site. This makes the blog model available in the Django admin interface.