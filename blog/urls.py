from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),              # 首页
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # 博客详情页
    path('blog/create/', views.blog_create, name='blog_create'),  # 写博客页面
]
