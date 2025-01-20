from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label='Введите логин',
        required=True,
        error_messages={'required': 'Поле "Логин" обязательно для заполнения.'}
    )
    password = forms.CharField(
        min_length=8,
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput,
        error_messages={'required': 'Поле "Пароль" обязательно для заполнения.'}
    )
    repeat_password = forms.CharField(
        min_length=8,
        label='Повторите пароль',
        required=True,
        widget=forms.PasswordInput,
        error_messages={'required': 'Поле "Повтор пароля" обязательно для заполнения.'}
    )
    age = forms.IntegerField(
        label='Введите свой возраст',
        required=True,
        error_messages={
            'required': 'Поле "Возраст" обязательно для заполнения.',
            'invalid': 'Возраст должен быть числом.'
        }
    )
