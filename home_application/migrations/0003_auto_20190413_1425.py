# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20190406_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.CharField(default=1, max_length=200, verbose_name='\u7c7b\u522b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='color',
            field=models.CharField(default=1, max_length=200, verbose_name='\u989c\u8272'),
            preserve_default=False,
        ),
    ]
