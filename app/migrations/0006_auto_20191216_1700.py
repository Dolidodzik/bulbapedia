# Generated by Django 2.2.3 on 2019-12-16 17:00

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191216_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='Evolves_from',
            field=djrichtextfield.models.RichTextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='creature',
            name='Evolves_to',
            field=djrichtextfield.models.RichTextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='creature',
            name='Fluff',
            field=djrichtextfield.models.RichTextField(default=''),
        ),
    ]
