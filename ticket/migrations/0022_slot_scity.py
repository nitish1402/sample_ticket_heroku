# Generated by Django 2.1.7 on 2019-03-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0021_slot_sid'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='scity',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
