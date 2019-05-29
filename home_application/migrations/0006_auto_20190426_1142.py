# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0005_auto_20190424_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=50, verbose_name='\u7528\u6237\u624b\u673a\u53f7'),
        ),
    ]
