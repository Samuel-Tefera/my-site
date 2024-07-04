from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('date',)
    prepopulated_fields = {
        'slug' : ('title',)
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)