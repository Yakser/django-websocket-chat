# Generated by Django 3.2.12 on 2022-05-05 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_messages', '0005_auto_20220505_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailychannelmessages',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='dailygroupmessages',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='userchannelmessage',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 5, 5, 19, 0, 35, 152147), null=True, verbose_name='Время отправки'),
        ),
        migrations.AlterField(
            model_name='usergroupmessage',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 5, 5, 19, 0, 35, 152147), null=True, verbose_name='Время отправки'),
        ),
    ]
