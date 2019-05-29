# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0006_auto_20190426_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=200, null=True, verbose_name='\u8ba2\u5355\u7f16\u53f7'),
        ),
    ]
