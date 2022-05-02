# Generated by Django 3.2.12 on 2022-05-02 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='user_id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
    ]
