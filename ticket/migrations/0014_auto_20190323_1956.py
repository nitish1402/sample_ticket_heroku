# Generated by Django 2.1.7 on 2019-03-23 14:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0013_auto_20190323_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='slist',
        ),
        migrations.AddField(
            model_name='sample',
            name='slist',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=30), blank=True, default='', size=None),
        ),
    ]
