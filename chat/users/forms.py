from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from users.validators import validate_login, validate_email

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'autofocus': True}), label='Почта')
    username = forms.CharField(
        widget=forms.HiddenInput(), required=False, label='')
    field_order = ['email', 'password']


class EditProfileForm(forms.Form):
    login = forms.CharField(max_length=150, label='Имя пользователя',
                            help_text='Максимум 150 символов', required=True)
    email = forms.EmailField(label='Почта', required=False)
  
    def validate_edit_login_and_email(self, current_user):
        login = self.cleaned_data['login']
        email = self.cleaned_data['email']

        if login != current_user.username and User.objects.filter(username=login):
            self.add_error(
                'login', 'Пользователь с таким именем уже существует!')
            return

        if email != current_user.email and User.objects.filter(email=email):
            self.add_error(
                'email', 'Пользователь с такой почтой уже существует!')
            return
        return True


class SignupForm(forms.Form):
    email = forms.CharField(max_length=200, label='Адрес электронной почты',
                            required=True, validators=[validate_email])
    login = forms.CharField(max_length=150, label='Имя пользователя',
                            help_text='Максимум 150 символов', required=True, validators=[validate_login])
    password = forms.CharField(max_length=255, label='Пароль',
                               help_text='Максимум 255 символов', widget=forms.PasswordInput, required=True, min_length=8)
    password_repeat = forms.CharField(max_length=255, label='Повторите пароль',
                                      widget=forms.PasswordInput)

    def check_passwords_match(self):
        password = self.cleaned_data['password']
        password_repeat = self.cleaned_data['password_repeat']

        if password != password_repeat:
            self.add_error('password_repeat', 'Пароли не совпадают!')
            return
        return password
