# -*- coding: utf-8 -*-
from django.db import models


class Goods(models.Model):
    goodsname = models.CharField(verbose_name=u'商品名称', max_length=50)
    goods_num = models.CharField(verbose_name=u'商品编号', max_length=50)
    img = models.CharField(verbose_name=u'商品图片', max_length=200)
    original_price = models.FloatField(verbose_name=u"原价")
    discount = models.FloatField(verbose_name=u"折扣", default=1.0)
    actual_price = models.FloatField(verbose_name=u"现价")
    material = models.CharField(verbose_name=u'材质', max_length=200)
    size = models.CharField(verbose_name=u'规格', max_length=200)
    stock = models.IntegerField(verbose_name=u'库存')
    category = models.CharField(verbose_name=u'类别', max_length=200)
    color = models.CharField(verbose_name=u'颜色', max_length=200)
    is_del = models.IntegerField(verbose_name=u'是否删除', default=0, null=True)

    class Meta:
        db_table = "goods"


class Order(models.Model):
    order_id = models.CharField(verbose_name=u'订单编号', max_length=200, null=True)
    total_price = models.FloatField(verbose_name=u'付款价格', max_length=50, null=True)
    order_time = models.DateTimeField(verbose_name=u'付款时间', null=True)
    goodsname = models.CharField(verbose_name=u'商品名称', max_length=50, null=True)
    goods_num = models.CharField(verbose_name=u'商品编号', max_length=50, null=True)
    user = models.CharField(verbose_name=u'用户名称', max_length=50, null=True)
    is_del = models.IntegerField(verbose_name=u'是否删除', default=0, null=True)
    goods_material = models.CharField(verbose_name=u'商品材质', max_length=50, null=True)
    goods_size = models.CharField(verbose_name=u'商品规格', max_length=50, null=True)
    goods_color = models.CharField(verbose_name=u'商品颜色', max_length=50, null=True)
    num = models.IntegerField(verbose_name=u'商品数量', null=True)
    order_status = models.IntegerField(verbose_name=u'订单状态', choices=((0, '等待发货'), (1, '已发货'), (2, '等待退款'),
                                                                      (3, '已退款')), default=0)

    class Meta:
        db_table = "order"


class User(models.Model):
    username = models.CharField(verbose_name=u'用户名', max_length=50)
    name = models.CharField(verbose_name=u'用户昵称', max_length=50)
    password = models.TextField(verbose_name=u'用户密码')
    address = models.TextField(verbose_name=u'收货地址', null=True)
    telephone = models.CharField(verbose_name=u'用户手机号', max_length=50)
    reputation = models.IntegerField(verbose_name=u'用户信誉', default=10)
    sex = models.IntegerField(verbose_name=u'用户性别', choices=((0, '女'), (1, '男')))
    last_time = models.DateTimeField(verbose_name=u'最后登录时间')
    is_del = models.IntegerField(verbose_name=u'是否删除', default=0)

    class Meta:
        db_table = "user"


class Shopcar(models.Model):
    goods_price = models.FloatField(verbose_name=u'付款价格', max_length=50, null=True)
    goodsname = models.CharField(verbose_name=u'商品名称', max_length=50, null=True)
    goods_num = models.CharField(verbose_name=u'商品编号', max_length=50, null=True)
    user = models.CharField(verbose_name=u'用户名称', max_length=50, null=True)
    is_del = models.IntegerField(verbose_name=u'是否删除', default=0, null=True)
    goods_material = models.CharField(verbose_name=u'商品材质', max_length=50, null=True)
    goods_size = models.CharField(verbose_name=u'商品规格', max_length=50, null=True)
    goods_color = models.CharField(verbose_name=u'商品颜色', max_length=50, null=True)
    num = models.IntegerField(verbose_name=u'商品数量', null=True)

    class Meta:
        db_table = "shopcar"

