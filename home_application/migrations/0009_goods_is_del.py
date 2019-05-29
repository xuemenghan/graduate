# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0008_shopcar'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_del',
            field=models.IntegerField(default=0, null=True, verbose_name='\u662f\u5426\u5220\u9664'),
        ),
    ]
