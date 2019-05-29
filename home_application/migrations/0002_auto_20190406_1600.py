# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='laset_time',
            new_name='last_time',
        ),
        migrations.AddField(
            model_name='goods',
            name='stock',
            field=models.IntegerField(default=1, verbose_name='\u5e93\u5b58'),
            preserve_default=False,
        ),
    ]
