from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    class Media:
        css = {'all':(
                'blog/css/simditor.css',
                )}
        js = (
                'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
                'blog/js/module.js',
                'blog/js/uploader.js',
                'blog/js/hotkeys.js',
                'blog/js/simditor.js',
                'blog/js/textarea.js',
)



admin.site.register(Post,admin_class=ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)



