# Generated by Django 3.2.12 on 2022-05-15 11:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users_messages', '0008_chatmessage_dailychatmessages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatMessage',
            new_name='UserChatMessage',
        ),
    ]
