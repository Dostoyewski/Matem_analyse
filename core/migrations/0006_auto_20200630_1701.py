# Generated by Django 3.0.7 on 2020-06-30 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200627_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='doc',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 17, 1, 18, 740120)),
        ),
    ]
