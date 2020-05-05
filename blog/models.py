from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    """分类表"""
    #1).一个类代表一个数据库表，表名默认是appname_classname  ----> blog_category
    #2). Django的数据库模型默认会添加ID作为主键，所以此处只需要创建分类名name即可
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Tag(models.Model):
    """标签表"""
    #1).
    #2). Django的数据库模型默认会添加ID作为主键，同上，此处只需要创建标签名即可
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Post(models.Model):
    """博客表"""
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文,我们使用了TextField
    body = models.TextField()
    # 这两个列分别表示文章的创建时间和最后一次修改时间,存储时间的字段用 DateTimeField 类型。
    #auto_now对象第一次创建时设置时间        auto_now_add 每次对象更新时更新时间
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    # 文章摘要,可以没有文章摘要,但默认情况下 CharField 要求我们必须存入数据,否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 新增views字段记录阅读量
    views = models.PositiveIntegerField(default=0)

    #分类：博客 = 1：N
    # on_delete=False在Django1.x版本默认是不级联删除的，可以不做设置. Django2.x一定要自 行指定.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    #标签：博客 = N:N
    tags = models.ManyToManyField(Tag,blank=True)

    # 自定义 get_absolute_url 方法 # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        #reverse相当于flask里面的url_for，根据视图函数名称反向获取对应的路由地址,因为视图函数名称不经常改变，路由地址可能会改变
        return reverse('detail', kwargs={'id': self.id})
    def __str__(self):
        return self.title

    # ...其它已有的模型方法  
    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])