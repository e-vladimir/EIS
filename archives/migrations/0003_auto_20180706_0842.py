# Generated by Django 2.0.6 on 2018-07-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0002_auto_20180705_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eis_archive',
            name='name',
        ),
        migrations.AddField(
            model_name='eis_archive',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
    ]
