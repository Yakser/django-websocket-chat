from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class CreateGroupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CreateGroupForm, self).__init__(*args, **kwargs)

        self.fields['group_members'].queryset = \
            User.objects.filter(~Q(id=self.user.id)).only('id', 'username')

    slug = forms.SlugField(label='Идентификатор',
                           help_text='Используйте буквы, цифры или @/./+/-/_ ',
                           max_length=100)

    name = forms.CharField(max_length=100,
                           label='Имя группы',
                           help_text='Максимум 100 символов',
                           required=True)

    group_members = forms.ModelMultipleChoiceField(
        label='Участники',
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)
