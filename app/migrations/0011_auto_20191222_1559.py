# Generated by Django 2.2.3 on 2019-12-22 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20191222_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='name',
            new_name='header',
        ),
    ]
