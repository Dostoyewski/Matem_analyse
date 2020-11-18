from django.contrib import admin
from .models import Post
# Register your models here.


class PostProfileAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('title', 'text', 'doc', 'order_id')


admin.site.register(Post, PostProfileAdmin)
