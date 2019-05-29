# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include

urlpatterns = patterns(
    'home_application.goods.views',
    (r'^show/$', 'show'),   # 首页更多推荐
    (r'^show_dis/$', 'show_dis'),   # 今日团购
    (r'^discount/$', 'discount'),   # 首页今日必抢
    (r'^get_details/$', 'get_details'),   # 商品详情
    (r'^in_cart/$', 'in_cart'),   # 加入购物车
    (r'^get_shopcart/$', 'get_shopcart'),   # 获取购物车列表
    (r'^delete_goods/$', 'delete_goods'),   # 删除购物车商品
    (r'^buy_goods/$', 'buy_goods'),   # 删除购物车商品
    (r'^search/$', 'search'),   # 模糊匹配
    (r'^pay/$', 'pay'),   # 付款
    (r'^get_order/$', 'get_order'),   # 订单列表
    (r'^get_order_admin/$', 'get_order_admin'),   # 管理员订单管理
    (r'^deliver_goods/$', 'deliver_goods'),   # 点击发货
    (r'^get_3/$', 'get_3'),   # 点击发货
    (r'^save_img/$', 'save_img'),   # 保存图片
    (r'^add_goods/$', 'add_goods'),   # 添加商品
    (r'^get_cate/$', 'get_cate'),   # 获取商品分类列表
    (r'^refund/$', 'refund'),   # 用户点击退款按钮，修改状态为等待退款
    (r'^back_refund/$', 'back_refund'),   # 商家回应退款请求
    (r'^del_good/$', 'del_good'),   # 删除表里面的商品
    (r'^get_goods_1/$', 'get_goods_1'),   # 编辑商品展示
    (r'^edit_good/$', 'edit_good'),   # 编辑商品保存
)

