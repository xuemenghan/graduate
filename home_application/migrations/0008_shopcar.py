# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0007_auto_20190427_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopcar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_price', models.FloatField(max_length=50, null=True, verbose_name='\u4ed8\u6b3e\u4ef7\u683c')),
                ('goodsname', models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('goods_num', models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u7f16\u53f7')),
                ('user', models.CharField(max_length=50, null=True, verbose_name='\u7528\u6237\u540d\u79f0')),
                ('is_del', models.IntegerField(default=0, null=True, verbose_name='\u662f\u5426\u5220\u9664')),
                ('goods_material', models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u6750\u8d28')),
                ('goods_size', models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u89c4\u683c')),
                ('goods_color', models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u989c\u8272')),
                ('num', models.IntegerField(null=True, verbose_name='\u5546\u54c1\u6570\u91cf')),
            ],
            options={
                'db_table': 'shopcar',
            },
        ),
    ]
