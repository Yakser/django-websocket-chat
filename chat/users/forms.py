from django import forms
from django.contrib.auth import get_user_model

from users.validators import validate_login, validate_email

User = get_user_model()


class EditProfileForm(forms.Form):
    login = forms.CharField(max_length=150,
                            label='Имя пользователя',
                            help_text='Максимум 150 символов',
                            required=True
                            )

    email = forms.EmailField(label='Почта',
                             required=False
                             )

    image = forms.ImageField(label='Аватар',
                             required=False,
                             allow_empty_file=False
                             )

    biography = forms.CharField(label='Расскажите немного о себе',
                                widget=forms.Textarea(),
                                max_length=500,
                                required=False
                                )

    def validate_edit_login(self, current_user):
        login = self.cleaned_data['login']
        
        if not current_user.is_staff:
            if len(login.strip()) < 8:
                self.add_error('login', 'Длина имени не менее 8 символов!')
                return

        if login != current_user.username and User.objects.filter(username=login):
            self.add_error('login',
                           'Пользователь с таким именем уже существует!')
            return

        return True

    def validate_edit_email(self, current_user):
        email = self.cleaned_data['email']

        if email != current_user.email and User.objects.filter(email=email):
            self.add_error('email',
                           'Пользователь с такой почтой уже существует!')
            return

        return True

    def validate_all(self, current_user):
        return self.validate_edit_email(current_user) and self.validate_edit_login(current_user)


class SignupForm(forms.Form):
    email = forms.CharField(max_length=200,
                            label='Адрес электронной почты',
                            widget=forms.EmailInput,
                            required=True,
                            validators=[validate_email])
    login = forms.CharField(max_length=150,
                            label='Имя пользователя',
                            help_text='Максимум 150 символов',
                            required=True,
                            validators=[validate_login])
    password = forms.CharField(max_length=255, label='Пароль',
                               help_text='Максимум 255 символов',
                               widget=forms.PasswordInput,
                               required=True,
                               min_length=8)
    password_repeat = forms.CharField(max_length=255,
                                      label='Повторите пароль',
                                      widget=forms.PasswordInput)

    def check_passwords_match(self):
        password = self.cleaned_data['password']
        password_repeat = self.cleaned_data['password_repeat']

        if password != password_repeat:
            self.add_error('password_repeat', 'Пароли не совпадают!')
            return
        return password
