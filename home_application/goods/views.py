# -*- coding: utf-8 -*-

import datetime
import json
import traceback
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models import Q

from common.mymako import render_json
from home_application import models


def show(req):
    """
    更多推荐
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        type = req.POST.get('type', '')
        if type == 'index_show':
            result = models.Goods.objects.filter(is_del=0).order_by('?')[:10]
        elif type == 'all_show':
            result = models.Goods.objects.filter(is_del=0)
        for i in result:
            dic = {'goodsname': i.goodsname, 'goods_num': i.goods_num, 'img': i.img, 'original_price': i.original_price,
                   'discount': i.discount, 'actual_price': i.actual_price, 'id': i.id}
            response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取商品列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def show_dis(req):
    """
    今日团购
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        result = models.Goods.objects.filter(is_del=0)
        for i in result:
            if i.discount != 1:
                dic = {'goodsname': i.goodsname, 'goods_num': i.goods_num, 'img': i.img,
                       'original_price': i.original_price,
                       'discount': i.discount, 'actual_price': i.actual_price}
                response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取商品列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def discount(req):
    """
    今日必抢
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        result = models.Goods.objects.filter(is_del=0).order_by('?')[:20]
        for i in result:
            if i.discount != 1.00:
                dic = {'goodsname': i.goodsname, 'goods_num': i.goods_num, 'img': i.img,
                       'original_price': i.original_price,
                       'discount': i.discount, 'actual_price': i.actual_price}
                if len(response['data']) < 4:
                    response['data'].append(dic)
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_details(req):
    """
    商品详情
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {'list': {}, 'material': [], 'color': [], 'size': []},
    }
    try:
        goods_num = req.POST.get('goods_num', '')
        obj = models.Goods.objects.get(goods_num=goods_num)
        response['data']['list'] = {'goodsname': obj.goodsname, 'goods_num': obj.goods_num, 'img': obj.img,
                            'original_price': obj.original_price, 'stock': obj.stock,
                            'discount': obj.discount, 'actual_price': obj.actual_price}

        for i in range(len(obj.material.split(','))):
            dic = {'material': obj.material.split(',')[i]}
            response['data']['material'].append(dic)
        dic = {}
        for i in range(len(obj.color.split(','))):
            dic = {'color': obj.color.split(',')[i]}
            response['data']['color'].append(dic)
        dic = {}
        for i in range(len(obj.size.split(','))):
            dic = {'size': obj.size.split(',')[i]}
            response['data']['size'].append(dic)
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取商品详情失败：%s' % e
        response['data'] = {}
    return render_json(response)


def in_cart(req):
    """
    加入购物车
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {},
    }
    try:
        goods_num = req.POST.get('goods_num', '')
        goodsname = req.POST.get('goodsname', '')
        material = req.POST.get('material', '')
        color = req.POST.get('color', '')
        size = req.POST.get('size', '')
        num = req.POST.get('num', '')
        username = req.POST.get('username', '')
        goods_price = float(models.Goods.objects.get(goods_num=goods_num).actual_price) * float(num)
        models.Shopcar.objects.create(
            goods_num=goods_num,
            goodsname=goodsname,
            goods_material=material,
            goods_color=color,
            goods_size=size,
            num=num,
            user=username,
            goods_price=goods_price
        )
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_shopcart(req):
    """
    获取购物车列表
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        username = req.POST.get('username', '')
        result = models.Shopcar.objects.filter(user=username, is_del=0)
        for i in result:
            obj = models.Goods.objects.get(goods_num=i.goods_num)
            dic = {
                'img': obj.img, 'goodsname': obj.goodsname, 'goods_num': obj.goods_num, 'actual_price': obj.actual_price,
                'num': i.num, 'id': i.id, 'goods_material': i.goods_material, 'goods_size': i.goods_size, 'goods_color': i.goods_color
            }
            response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取购物车列表失败：%s' % e
        response['data'] = {}
    return render_json(response)


def delete_goods(req):
    """
    删除购物车商品
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        id = req.POST.get('id', '')
        obj = models.Shopcar.objects.get(id=id)
        obj.is_del = 1
        obj.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def del_good(req):
    """
    删除购物车商品
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        id = req.POST.get('id', '')
        obj = models.Goods.objects.get(id=id)
        obj.is_del = 1
        obj.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def buy_goods(req):
    """
    付款商品
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        id = req.POST.get('id', '')
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def search(req):
    """
    付款商品
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        name = req.POST.get('name', '')
        q = Q()
        q.add(Q(goodsname__contains=name) | Q(category__contains=name) | Q(is_del=0), q.AND)
        search_data = models.Goods.objects.filter(q)
        for i in search_data:
            dic = {'goodsname': i.goodsname, 'goods_num': i.goods_num, 'img': i.img, 'original_price': i.original_price,
                   'discount': i.discount, 'actual_price': i.actual_price}
            response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def pay(req):
    """
    付款
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        arr = json.loads(req.POST.get('arr', ''))
        print arr
        price = req.POST.get('price', '')
        username = req.POST.get('username', '')
        result = models.Shopcar.objects.filter(user=username, is_del=0)
        uu = uuid.uuid4()
        for i in range(len(arr)):
            for j in result:
                if j.goods_num == arr[i]:
                    j.is_del = 1
                    models.Order.objects.create(
                        order_id=uu,
                        order_time=datetime.datetime.now(),
                        goodsname=j.goodsname,
                        goods_num=j.goods_num,
                        user=username,
                        goods_material=j.goods_material,
                        goods_size=j.goods_size,
                        goods_color=j.goods_color,
                        num=j.num,
                    )
                    j.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_order(req):
    """
    获取订单列表
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        username = req.POST.get('username', '')
        result = models.Order.objects.filter(user=username, is_del=0).values('order_id').distinct()
        for i in range(len(result)):
            list = []
            list.append(result[i])
            response['data'].append(list)
        order = models.Order.objects.filter(user=username, is_del=0)

        for i in order:
            if i.order_id != None:
                obj = models.Goods.objects.get(goods_num=i.goods_num)
                dic = {'order_id': i.order_id, 'total_price': i.num * obj.actual_price,
                       'order_time': i.order_time.strftime('%Y-%m-%d'),
                       'goodsname': i.goodsname, 'order_status': i.get_order_status_display(), 'goods_color': i.goods_color,
                       'goods_size': i.goods_size, 'goods_material': i.goods_material, 'goods_num': i.goods_num,
                       'num': i.num, 'img': obj.img, 'id': i.id}
                for j in response['data']:
                    if j[0]['order_id'] == dic['order_id']:
                        j.append(dic)
        for i in response['data']:
            i.pop(0)
            if i == []:
                response['data'].remove([])
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_order_admin(req):
    """
    获取订单列表
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        result = models.Order.objects.filter(is_del=0).values('order_id').distinct()
        for i in range(len(result)):
            list = []
            if result[i]['order_id'] != None:
                list.append(result[i])
                response['data'].append(list)
        order = models.Order.objects.filter(is_del=0)

        for i in order:
            if i.order_id != None:
                obj = models.Goods.objects.get(goods_num=i.goods_num)
                dic = {'order_id': i.order_id, 'total_price': i.num * obj.actual_price,
                       'order_time': i.order_time.strftime('%Y-%m-%d %H:%M:%S'),
                       'goodsname': i.goodsname, 'order_status': i.get_order_status_display(), 'goods_color': i.goods_color,
                       'goods_size': i.goods_size, 'goods_material': i.goods_material, 'goods_num': i.goods_num,
                       'num': i.num, 'img': obj.img, 'id': i.id}
                for j in response['data']:
                    if j[0]['order_id'] == dic['order_id']:
                        j.append(dic)
        for i in response['data']:
            i.pop(0)
            if i == []:
                response['data'].remove([])
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def deliver_goods(req):
    """
    点击发货
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        id = req.POST.get('id', '')
        result = models.Order.objects.filter(id=id, is_del=0)
        for i in result:
            i.order_status = 1
            i.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def refund(req):
    """
    用户点击退款，修改状态为等待退款
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        id = req.POST.get('id', '')
        result = models.Order.objects.filter(id=id, is_del=0)
        for i in result:
            i.order_status = 2
            i.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def back_refund(req):
    """
    商家回应退款请求
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        id = req.POST.get('id', '')
        result = models.Order.objects.filter(id=id, is_del=0)
        for i in result:
            i.order_status = 3
            i.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_3(req):
    """
    随机显示三个商品
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        result = models.Goods.objects.filter(is_del=0).order_by('?')[:3]
        for i in result:
            dic = {'goodsname': i.goodsname, 'goods_num': i.goods_num, 'img': i.img, 'original_price': i.original_price,
                   'discount': i.discount, 'actual_price': i.actual_price}
            response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def save_img(req):
    """
    添加商品
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {},
    }
    try:
        img = req.FILES.get('file')
        path = default_storage.save('F:\\Pycharm\\bishe\\graduate\\static\\img\\'+img.name, ContentFile(img.read()))
        path = path.split('graduate')
        img = path[1]
        response['data'] = {'img': img}
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_cate(req):
    """
    获取商品类别列表
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        result = models.Goods.objects.filter(is_del=0).values('category').distinct()
        for i in result:
            dic = {'category': i['category']}
            response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def add_goods(req):
    """
    添加商品
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        material = req.POST.get('material', '')
        size = req.POST.get('size', '')
        color = req.POST.get('color', '')
        category = req.POST.get('category', '')
        discount = req.POST.get('disc', '')
        goodsname = req.POST.get('goodsname', '')
        goods_num = req.POST.get('goods_num', '')
        original_price = req.POST.get('original_price', '')
        stock = req.POST.get('stock', '')
        img = req.POST.get('imageUrl', '')
        models.Goods.objects.create(
            goodsname=goodsname,
            goods_num=goods_num,
            img=img,
            original_price=original_price,
            discount=discount,
            actual_price=float(original_price) * float(discount),
            material=material,
            size=size,
            stock=stock,
            category=category,
            color=color
        )
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_goods_1(req):
    """
    编辑商品展示信息
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {},
    }
    try:
        id = req.POST.get('id', '')
        obj = models.Goods.objects.get(id=id)
        dic = {'goodsname': obj.goodsname, 'goods_num': obj.goods_num, 'img': obj.img, 'original_price': obj.original_price,
               'discount': obj.discount, 'actual_price': obj.actual_price, 'id': obj.id,
               'material': obj.material, 'size': obj.size, 'stock': obj.stock, 'category': obj.category,
               'color': obj.color}
        response['data'] = dic
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def edit_good(req):
    """
    编辑商品保存
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        id = req.POST.get('id', '')
        material = req.POST.get('material', '')
        size = req.POST.get('size', '')
        color = req.POST.get('color', '')
        category = req.POST.get('category', '')
        discount = req.POST.get('discount', '')
        goodsname = req.POST.get('goodsname', '')
        goods_num = req.POST.get('goods_num', '')
        original_price = req.POST.get('original_price', '')
        actual_price = req.POST.get('actual_price', '')
        stock = req.POST.get('stock', '')
        img = req.POST.get('img', '')
        obj = models.Goods.objects.get(id=id)
        obj.goodsname = goodsname
        obj.goods_num = goods_num
        obj.img = img
        obj.original_price = original_price
        obj.discount = discount
        obj.actual_price = actual_price
        obj.material = material
        obj.size = size
        obj.stock = stock
        obj.category = category
        obj.color = color
        obj.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


