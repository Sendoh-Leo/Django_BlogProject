#coding:utf-8
#date:2020/5/410:54
#author:CQ_Liu

from django.conf.urls import url
from . import views

#什么都不做的时候，跳转到视图函数
#处理post/1的url请求
urlpatterns = [ url(r'^$', views.index, name='index'),
                #^以什么开头，$以什么结尾，[0-9]指单个数字，+代表前面的字符出现一次或多次
                #(?P<id>[0-9]+)关键字匹配，把满足正则规则[0-9]+的字符传给关键字id，该id作为关键字传给视图函数view.detail
                url(r'^post/(?P<id>[0-9]+)/$', views.detail, name='detail'),

                #获取指定分类信息的路由,并在视图函数中创建category函数
                url(r'^category/(?P<id>[0-9]+)/$', views.category, name='category'),

                #获取指定归档日期的路由，并在视图函数中创建archives函数
                url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
                #获取指定标签云的路由，并在视图函数中创建tage函数
                url(r'^tag/(?P<id>[0-9]+)/$', views.tag, name='tag'),
                ]