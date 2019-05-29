# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20190413_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='goods_color',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u989c\u8272'),
        ),
        migrations.AddField(
            model_name='order',
            name='goods_material',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u6750\u8d28'),
        ),
        migrations.AddField(
            model_name='order',
            name='goods_num',
            field=models.IntegerField(max_length=50, null=True, verbose_name='\u5546\u54c1\u6570\u91cf'),
        ),
        migrations.AddField(
            model_name='order',
            name='goods_size',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u89c4\u683c'),
        ),
        migrations.AlterField(
            model_name='order',
            name='goodsname',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_del',
            field=models.IntegerField(default=0, null=True, verbose_name='\u662f\u5426\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=50, null=True, verbose_name='\u8ba2\u5355\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(null=True, verbose_name='\u4ed8\u6b3e\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(max_length=50, null=True, verbose_name='\u4ed8\u6b3e\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.CharField(max_length=50, null=True, verbose_name='\u7528\u6237\u540d\u79f0'),
        ),
    ]
