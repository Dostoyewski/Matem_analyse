# Generated by Django 3.0.7 on 2020-06-26 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('text', models.CharField(blank=True, max_length=1000)),
                ('published', models.DateTimeField(default=datetime.datetime(2020, 6, 26, 14, 25, 9, 235385))),
            ],
        ),
    ]
