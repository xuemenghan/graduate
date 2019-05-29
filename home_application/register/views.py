# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
import json, datetime, traceback

from home_application import models


def register(req):
    """
    申请
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {'list': []},
    }
    try:
        username = req.POST.get('username', '')
        name = username
        password = req.POST.get('pass', '')
        telephone = req.POST.get('telephone', '')
        sex = req.POST.get('sex', '')
        address = req.POST.get('address', '')
        last_time = datetime.datetime.now()

        # username = req.POST

        models.User.objects.create(
            username=username,
            name=name,
            password=password,
            telephone=telephone,
            sex=sex,
            address=address,
            last_time=last_time,
        )
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def login(req):
    """
    登录
    :param req:
    :return:
    """
    print 1111
    response = {
        'result': True,
        'code': 1,
        'message': 'success',
    }

    username = req.POST.get('username', '')
    password = req.POST.get('password', '')
    result = models.User.objects.all()
    for i in result:
        if username == i.username and password == i.password:
            response['code'] = 0    # 正常
            last_time = datetime.datetime.now()
            i.last_time = last_time
            i.save()
            break
    # 1 为验证失败
    return render_json(response)


def get_cus(req):
    """
    获取客户列表
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
        result = models.User.objects.filter(is_del=0)
        for i in result:
            dic = {
                'name': i.name, 'address': i.address, 'telephone': i.telephone, 'sex': i.get_sex_display(),
                'last_time': i.last_time.strftime('%Y-%m-%d'),'id': i.id
            }
            response['data'].append(dic)
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def dele_cus(req):
    """
    删除客户
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
        obj = models.User.objects.get(id=id)
        obj.is_del = 1
        obj.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'删除失败：%s' % e
        response['data'] = {}
    return render_json(response)


def get_info(req):
    """
    获取个人信息
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
        username = req.POST.get('username', '')
        obj = models.User.objects.get(username=username)
        response['data'] = {
            'username': obj.username, 'name': obj.name, 'password': obj.password, 'address': obj.address,
            'telephone': obj.telephone, 'sex': obj.sex
        }
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'删除失败：%s' % e
        response['data'] = {}
    return render_json(response)


def edit_info(req):
    """
    修改个人信息
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
        info = req.POST.getlist('info', '')
        info = json.loads(info[0])
        obj = models.User.objects.get(username=info["username"])
        obj.telephone = info["telephone"]
        obj.sex = info["sex"]
        obj.password = info["password"]
        obj.name = info["name"]
        obj.address = info["address"]
        obj.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'删除失败：%s' % e
        response['data'] = {}
    return render_json(response)
