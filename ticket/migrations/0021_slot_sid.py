# Generated by Django 2.1.7 on 2019-03-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0020_slot_sstat'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='sid',
            field=models.IntegerField(default=0),
        ),
    ]