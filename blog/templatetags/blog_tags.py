#coding:utf-8
#date:2020/5/422:02
#author:CQ_Liu
from django import template
from django.db.models import Count

from blog.models import Post, Category,Tag

# 创建模板库对象
register = template.Library()
# 编写查询罪行博客信息的，并将函数函数 get_recent_posts添加到模板中
#最新文章模板
@register.simple_tag
def get_recent_posts(num=5):
    posts = Post.objects.all().order_by('-created_time')[:num]
    return posts
#归档模板
@register.simple_tag
def archives():
    # created_time即 Post 的创建时间，month 是精度， order='DESC' 表明降序排列
    return Post.objects.dates('created_time', 'month', order='DESC')
#分类模板
# @register.simple_tag
# def get_categories(): # 别忘了在顶部引入 Category 类
#     return Category.objects.all()

#标签模板
@register.simple_tag
def get_tags(): # 别忘了在顶部引入 Category 类
    return Tag.objects.all()

@register.simple_tag
def get_categories():
# 记得在顶部引入count函数  #Count计算分类下的文章数，其接受的参数为需要计数的模型的名称 
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
