# Generated by Django 2.2.3 on 2019-12-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191216_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('Breed_name', models.CharField(default='', max_length=150)),
                ('Type', models.CharField(default='', max_length=150)),
                ('Element', models.CharField(default='', max_length=150)),
                ('Frequency', models.CharField(default='', max_length=150)),
                ('Diet', models.CharField(default='', max_length=150)),
                ('Role', models.CharField(default='', max_length=150)),
                ('Hunger', models.CharField(default='', max_length=150)),
                ('Strong_VS', models.CharField(default='', max_length=150)),
                ('Weak_VS', models.CharField(default='', max_length=150)),
                ('Attacks', models.CharField(default='', max_length=150)),
                ('Strength', models.CharField(default='', max_length=150)),
                ('Speed', models.CharField(default='', max_length=150)),
                ('Agility', models.CharField(default='', max_length=150)),
                ('Endurance', models.CharField(default='', max_length=150)),
                ('Durability', models.CharField(default='', max_length=150)),
                ('Other_Enchancements', models.CharField(default='', max_length=500)),
                ('Evolves_from', models.CharField(default='', max_length=500)),
                ('Evolves_to', models.CharField(default='', max_length=500)),
                ('Fluff', models.TextField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='homepage',
            name='name',
            field=models.CharField(default='This will be displayed as header of your page, edit it in admin panel!', max_length=150),
        ),
    ]