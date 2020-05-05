import markdown
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse

from blog.models import Post, Category,Tag


def index(request):
    #用字典存放要传入前端模板的参数
    posts = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={ 'posts':posts })

def detail(request,id):
    #通过id寻找Post,找到了返回post = 当前id所属的Post，找不到返回404
    post = get_object_or_404(Post, id =id)
    #把post的内容传到html模板中
    # 记得在顶部引入 markdown 模块
    # extensions，它是对 Markdown 语法的拓展，这里我们使用了三个拓展
    #           1). extra 本身包含很多拓展，
    #           2). codehilite 是语法高亮拓展
    #           3). toc 则允许我们自动生成目录
    post.body = markdown.markdown(post.body,
                                  extensions=['markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc', ])

    post.increase_views()
    return render(request, 'blog/detail.html', context={'post': post})

def category(request,id):
    """根据分类的id显示所有的博客信息"""
    #获取分类对象
    cate = get_object_or_404(Category, id=id)
    #通过分类对象找到所包含的博客信息
    cate_list = Post.objects.filter(category=cate).order_by('-created_time')
    #返回到相关的前端页面
    return render(request, 'blog/index.html', context={'posts': cate_list})

def archives(request,year,month):
    date_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'posts': date_list})

def tag(request,id):
    # 获取标签对象
    tag = get_object_or_404(Tag, id=id)
    # 通过分类对象找到所包含的博客信息
    tag_list = Post.objects.filter(tags=tag).order_by('-created_time')
    # 返回到相关的前端页面
    return render(request, 'blog/index.html', context={'posts':tag_list})