from django.contrib.auth import get_user_model
from django.forms import ValidationError

User = get_user_model()


def validate_login(value):
    if len(value.strip()) < 2:
        raise ValidationError('Длина не менее 2 символов!')
    if User.objects.filter(username=value):
        raise ValidationError('Пользователь с таким именем уже существует!')


def validate_email(value):
    if User.objects.filter(email=value):
        raise ValidationError('Пользователь с такой почтой уже существует!')


def validate_edit_login(current_user):
    def wrapper(login):
        if login != current_user.username and User.objects.filter(username=login):
            raise ValidationError(
                'Пользователь с таким именем уже существует!')

    return wrapper


def validate_edit_email(current_user):
    def wrapper(email):
        if email != current_user.email and User.objects.filter(email=email):
            raise ValidationError(
                'Пользователь с такой почтой уже существует!')
    return wrapper
