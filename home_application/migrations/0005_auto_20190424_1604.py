# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_auto_20190423_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='num',
            field=models.IntegerField(null=True, verbose_name='\u5546\u54c1\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='order',
            name='goods_num',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u7f16\u53f7'),
        ),
    ]
