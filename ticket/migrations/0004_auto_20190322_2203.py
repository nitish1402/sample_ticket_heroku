# Generated by Django 2.1.7 on 2019-03-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20190322_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treg',
            name='tafter_name',
            field=models.CharField(blank=True, default='No Movie Name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='teve_name',
            field=models.CharField(blank=True, default='No Movie Name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tloc',
            field=models.CharField(blank=True, default='Please update theatre location', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tmorn_name',
            field=models.CharField(blank=True, default='No Movie Name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tname',
            field=models.CharField(blank=True, default='Please update theatre name', max_length=30, null=True),
        ),
    ]