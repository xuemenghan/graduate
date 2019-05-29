# -*- coding: utf-8 -*-
import base64
import json
import traceback

from account.decorators import login_exempt
from common.mymako import render_json
from home_application import models
from home_application.utils.ESB import ESBApi, ESBComponentApi


def get_apps(req):
    """
    获取主机
    :param request:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {'list': []},
    }
    try:
        result = ESBApi(req).search_business()
        if result['result']:
            if len(result['data']['info']) > 0:
                for item in result['data']['info']:
                    dic = {}
                    dic['id'] = item['bk_biz_id']
                    dic['name'] = item['bk_biz_name']
                    response['data']['list'].append(dic)
            else:
                response['result'] = False
                response['code'] = 1
                response['message'] = u'该用户下无业务'
                response['data'] = {'list': []}

    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_set(req):
    """
    获取集群
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {'list': []},
    }
    try:
        biz_id = req.GET.get('biz_id', '')
        result = ESBApi(req).get_set(bk_biz_id=biz_id)
        for i in result['data']['info']:
            dic = {'bk_set_id': i['bk_set_id'], 'bk_set_name': i['bk_set_name']}
            response['data']['list'].append(dic)
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_hosts(req):
    """
    根据biz_id获取主机
    data=[{ip:bk_host_innerip},{os_type:bk_os_name},{cloud_id:bk_cloud_id[0][bk_inst_id]},
         {cloud_name:bk_cloud_id[0][bk_obj_name]}]
    :param req:
    :return:
    """
    response = {}

    try:
        biz_id = req.GET.get("biz_id", "")
        set_id = req.GET.get("set_id", "")
        module_id = req.GET.get("module_id", "")
        result = ESBApi(req).search_host(bk_biz_id=biz_id, set_id=set_id, module_id=module_id)
        if result['result']:
            response['result'] = True
            response['code'] = 0
            response['message'] = 'success'
            response['data'] = {'list': []}

            if len(result['data']) > 0:
                for item in result['data']['info']:
                    dic = {}
                    dic['ip'] = item['host']['bk_host_innerip']
                    dic['os_type'] = item['host']['bk_os_name']
                    dic['cloud_id'] = item['host']['bk_cloud_id'][0]['bk_inst_id']
                    dic['cloud_name'] = item['host']['bk_cloud_id'][0]['bk_inst_name']
                    response['data']['list'].append(dic)
        else:
            response['result'] = True
            response['code'] = 0
            response['message'] = u'该用户下无主机'
            response['data'] = {}
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取主机列表失败：%s' % e
        response['data'] = {}
    return render_json(response)


def search_module(req):
    """
    根据biz_id,bk_set_id查询模块
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {'list': []},
    }
    try:
        bk_biz_id = req.GET.get('biz_id', '')
        bk_set_id = req.GET.get('set_id', '')
        result = ESBApi(req).search_module(bk_biz_id=bk_biz_id, bk_set_id=bk_set_id)
        if len(result['data']) > 0:
            for item in result['data']['info']:
                dic = {
                    'bk_module_id': item['bk_module_id'],
                    'bk_module_name': item['bk_module_name']
                }
                response['data']['list'].append(dic)
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def fast_script(req):
    """
    执行
    :param req:
    :return:
    """
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {'list': []},
    }
    try:
        bk_biz_id = req.GET.get('biz_id', '')
        biz_name = req.GET.get('biz_name', '')
        module_name = req.GET.get('module_name', '')
        set_name = req.GET.get('set_name', '')
        username = req.user.username
        ips = req.GET.get('ips', '').split(",")
        # obj = models.Script.objects.get(id=1)
        # script_input = obj.script_content
        # script_type = obj.type
        ip_list = []
        for i in range(0, len(ips), 2):
            dic = {
                'bk_cloud_id': int(ips[i+1]),
                'ip': ips[i]
            }
            ip_list.append(dic)
        # print ip_list, script_input
        # result = ESBApi(req).fast_execute_script(script_content=base64.b64encode(script_input), ip_list=ip_list,
        #                                          bk_biz_id=bk_biz_id, script_type=script_type)
        # print result
        # job_instance_id = result['data']['job_instance_id']
        ip_list = json.dumps(ip_list)
        models.Record.objects.create(
            # job_instance_id=job_instance_id,
            biz_id=bk_biz_id,
            biz_name=biz_name,
            module_name=module_name,
            set_name=set_name,
            ips=ip_list,
            username=username,
        )
        # loop(req)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


def get_record(req):
    """
    获取记录
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
        result = models.Record.objects.all()
        for i in result:
            ip = []
            dic = {
                'id': i.id, 'username': i.username, 'biz_name': i.biz_name, 'set_name': i.set_name,
                'module_name': i.module_name, 'is_start': i.is_start, 'start_time': i.start_time.strftime('%Y-%m-%d')
            }
            ips = json.loads(i.ips)
            for j in range(len(ips)):
                ip.append(ips[j]['ip'])
            dic['ip'] = ip
            response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = []
    return render_json(response)


def loop():
    """
    周期执行脚本
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
        record = models.Record.objects.all()
        obj = models.Script.objects.get(id=1)
        for i in record:
            if i.is_start == 1:
                script_input = obj.script_content
                ip_list = json.loads(i.ips)
                bk_biz_id = i.biz_id
                script_type = obj.type
                result = ESBComponentApi().fast_execute_script(script_content=base64.b64encode(script_input),
                                                              ip_list=ip_list,
                                                              bk_biz_id=bk_biz_id, script_type=script_type)
                while True:
                    job_instance_id = result['data']['job_instance_id']
                    instance = ESBComponentApi().get_job_instance_log(bk_biz_id=bk_biz_id, job_instance_id=job_instance_id)
                    status = instance['data'][0]['status']
                    if status == 3 or status == 4:
                        break
                log = instance['data'][0]['step_results'][0]['ip_logs'][0]['log_content']
                # rate = rate.split('|')
                # print rate
                # cpu_rate = rate[1]
                # memory_rate = rate[2]
                # disk_rate = rate[3]

                models.Result.objects.create(
                    job_instance_id=result['data']['job_instance_id'],
                    result=result['result'],
                    record=i,
                    # cpu_rate=cpu_rate,
                    # memory_rate=memory_rate,
                    # disk_rate=disk_rate,
                    log=log,
                )
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = []
    return render_json(response)


def change(req):
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        record_id = req.GET.get('record_id', '')
        obj = models.Record.objects.get(id=record_id)
        if obj.is_start == 0:
            obj.is_start = 1
        elif obj.is_start == 1:
            obj.is_start = 0
        obj.save()
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = []
    return render_json(response)


def search(req):
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        start_time = req.GET.get('start_time', '')
        # end_time = req.GET.get('end_time', '')
        result = models.Record.objects.all()
        for i in result:
            u = i.start_time.strftime('%Y-%m-%d')
            if u < start_time:
                obj = models.Record.objects.filter(id=i.id)
                for j in obj:
                    ip = []
                    dic = {
                        'id': j.id, 'username': j.username, 'biz_name': j.biz_name, 'set_name': j.set_name,
                        'module_name': j.module_name, 'is_start': j.is_start,
                        'start_time': j.start_time.strftime('%Y-%m-%d')
                    }
                    ips = json.loads(i.ips)
                    for p in range(len(ips)):
                        ip.append(ips[p]['ip'])
                    dic['ip'] = ip
                    response['data'].append(dic)
    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = []
    return render_json(response)


def get_detail(req):
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': [],
    }
    try:
        record_id = req.GET.get('record_id', '')
        obj = models.Result.objects.get(record=record_id)
        obj1 = models.Record.objects.get(id=record_id)
        response['data'] = {
            'job_instance_id': obj.job_instance_id, 'log': obj.log, 'ips': obj1.ips
        }

    except Exception, e:
        traceback.print_exc()
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = []
    return render_json(response)



@login_exempt
def inp(req):
    response = {
        'result': True,
        'code': 0,
        'message': 'success',
        'data': {'list': []},
    }
    try:
        script = '''#!/bin/bash
            MEMORY =$(free - m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
            DISK =$(df - h | awk '$NF=="/"{printf "%s", $5}')
            CPU =$(top - bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
            DATE =$(date "+%Y-%m-%d %H:%M:%S")
            echo - e
            "$DATE|$MEMORY|$DISK|$CPU"'''
        models.Script.objects.create(
                name='脚本',
                type=1,
                script_content=script,
            )
    except Exception, e:
        response['result'] = False
        response['code'] = 1
        response['message'] = u'获取业务列表失败：%s' % e
        response['data'] = {'list': []}
    return render_json(response)


