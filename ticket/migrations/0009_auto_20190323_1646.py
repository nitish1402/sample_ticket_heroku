# Generated by Django 2.1.7 on 2019-03-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_treg_tcity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treg',
            name='tcity',
            field=models.CharField(blank=True, default='Please update', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tloc',
            field=models.CharField(blank=True, default='Please update', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tname',
            field=models.CharField(blank=True, default='Please update', max_length=30, null=True),
        ),
    ]