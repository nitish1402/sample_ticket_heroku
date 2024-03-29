# Generated by Django 2.1.7 on 2019-03-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20190322_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treg',
            name='tafter_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tafter_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tcost',
            field=models.IntegerField(blank=True, default=150, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='teve_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='treg',
            name='teve_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tloc',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tmorn_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tmorn_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treg',
            name='tname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
