# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodsname', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('goods_num', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u7f16\u53f7')),
                ('img', models.CharField(max_length=200, verbose_name='\u5546\u54c1\u56fe\u7247')),
                ('original_price', models.FloatField(verbose_name='\u539f\u4ef7')),
                ('discount', models.FloatField(default=1.0, verbose_name='\u6298\u6263')),
                ('actual_price', models.FloatField(verbose_name='\u73b0\u4ef7')),
                ('material', models.CharField(max_length=200, verbose_name='\u6750\u8d28')),
                ('size', models.CharField(max_length=200, verbose_name='\u89c4\u683c')),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=50, verbose_name='\u8ba2\u5355\u7f16\u53f7')),
                ('total_price', models.FloatField(max_length=50, verbose_name='\u4ed8\u6b3e\u4ef7\u683c')),
                ('order_time', models.DateTimeField(verbose_name='\u4ed8\u6b3e\u65f6\u95f4')),
                ('goodsname', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('user', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d\u79f0')),
                ('is_del', models.IntegerField(default=0, verbose_name='\u662f\u5426\u5220\u9664')),
                ('order_status', models.IntegerField(default=0, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(0, b'\xe7\xad\x89\xe5\xbe\x85\xe5\x8f\x91\xe8\xb4\xa7'), (1, b'\xe5\xb7\xb2\xe5\x8f\x91\xe8\xb4\xa7'), (2, b'\xe7\xad\x89\xe5\xbe\x85\xe9\x80\x80\xe6\xac\xbe'), (3, b'\xe5\xb7\xb2\xe9\x80\x80\xe6\xac\xbe')])),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('name', models.CharField(max_length=50, verbose_name='\u7528\u6237\u6635\u79f0')),
                ('password', models.TextField(verbose_name='\u7528\u6237\u5bc6\u7801')),
                ('address', models.TextField(null=True, verbose_name='\u6536\u8d27\u5730\u5740')),
                ('telephone', models.IntegerField(verbose_name='\u7528\u6237\u624b\u673a\u53f7')),
                ('reputation', models.IntegerField(default=10, verbose_name='\u7528\u6237\u4fe1\u8a89')),
                ('sex', models.IntegerField(verbose_name='\u7528\u6237\u6027\u522b', choices=[(0, b'\xe5\xa5\xb3'), (1, b'\xe7\x94\xb7')])),
                ('laset_time', models.DateTimeField(verbose_name='\u6700\u540e\u767b\u5f55\u65f6\u95f4')),
                ('is_del', models.IntegerField(default=0, verbose_name='\u662f\u5426\u5220\u9664')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
