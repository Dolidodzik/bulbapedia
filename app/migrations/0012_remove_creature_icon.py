# Generated by Django 2.2.3 on 2019-12-22 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20191222_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creature',
            name='icon',
        ),
    ]
