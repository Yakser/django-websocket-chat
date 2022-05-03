# Generated by Django 3.2.12 on 2022-05-03 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_channels', '0004_auto_20220503_2144'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_auto_20220503_2144'),
        ('users_messages', '0002_auto_20220502_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMessagesChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_containers', to='users_channels.userschannel', verbose_name='Канал')),
            ],
            options={
                'verbose_name': 'Контейнер сообщений',
                'verbose_name_plural': 'Контейнеры сообщений',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DailyMessagesGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_containers', to='groups.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Контейнер сообщений',
                'verbose_name_plural': 'Контейнеры сообщений',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserChannelMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024, verbose_name='Текст')),
                ('datetime', models.DateTimeField()),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_messages', to='users_messages.dailymessageschannel', verbose_name='Контейнер')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_messages', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024, verbose_name='Текст')),
                ('datetime', models.DateTimeField()),
                ('container', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_messages', to='users_messages.dailymessagesgroup', verbose_name='Контейнер')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_messages', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
    ]
