# Generated by Django 2.1.7 on 2019-03-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0016_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.AddField(
            model_name='movie',
            name='mcity',
            field=models.CharField(default='', max_length=30),
        ),
    ]