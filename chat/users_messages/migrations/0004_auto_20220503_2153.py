# Generated by Django 3.2.12 on 2022-05-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_messages', '0003_auto_20220503_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailymessageschannel',
            options={'verbose_name': 'Контейнер сообщений канала', 'verbose_name_plural': 'Контейнеры сообщений канала'},
        ),
        migrations.AlterModelOptions(
            name='dailymessagesgroup',
            options={'verbose_name': 'Контейнер сообщений группы', 'verbose_name_plural': 'Контейнеры сообщений группы'},
        ),
        migrations.AlterModelOptions(
            name='userchannelmessage',
            options={'verbose_name': 'Сообщение канала', 'verbose_name_plural': 'Сообщения канала'},
        ),
        migrations.AlterModelOptions(
            name='usergroupmessage',
            options={'verbose_name': 'Сообщение группы', 'verbose_name_plural': 'Сообщения группы'},
        ),
        migrations.RemoveField(
            model_name='userchannelmessage',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='usergroupmessage',
            name='datetime',
        ),
        migrations.AddField(
            model_name='userchannelmessage',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='Время отправки'),
        ),
        migrations.AddField(
            model_name='usergroupmessage',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='Время отправки'),
        ),
    ]