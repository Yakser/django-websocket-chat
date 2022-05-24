from django.forms import ValidationError

from groups.models import Group


def validate_slug(value: str):
    if len(value.strip()) < 2:
        raise ValidationError('Длина не менее 2 символов!')
    if Group.objects.filter(slug=value):
        raise ValidationError('Группа с таким идентификатором уже существует!')
