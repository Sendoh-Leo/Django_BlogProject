from django.contrib import admin

# Register your models here.
# blog/admin.py

from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    #列表中的内容为models中博客表中创建的类名
    list_display = ['title', 'created_time', 'modified_time', 'category']
    #增加链接
    list_display_links = ['title','created_time']
    #添加搜索项
    search_fields = ['title']
    #每页显示数据
    list_per_page = 5



admin.site.register(Post,PostAdmin)  #新增定制的PostAdmin
admin.site.register(Category)
admin.site.register(Tag)

