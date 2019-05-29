# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include

urlpatterns = patterns(
    'home_application.register.views',
    (r'^register/$', 'register'),
    (r'^login/$', 'login'),
    (r'^get_cus/$', 'get_cus'),  # 客户列表
    (r'^dele_cus/$', 'dele_cus'),  # 删除客户
    (r'^get_info/$', 'get_info'),  # 获取个人信息
    (r'^edit_info/$', 'edit_info'),  # 修改个人信息
)

