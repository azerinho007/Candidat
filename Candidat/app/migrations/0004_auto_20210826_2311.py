# Generated by Django 2.2.24 on 2021-08-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210826_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taburl',
            name='nb',
            field=models.IntegerField(default=0),
        ),
    ]
