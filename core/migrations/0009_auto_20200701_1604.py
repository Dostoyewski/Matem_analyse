# Generated by Django 3.0.7 on 2020-07-01 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200630_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 16, 4, 28, 650569)),
        ),
    ]