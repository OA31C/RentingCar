from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name in ('email', 'username', 'password1', 'password2'):
            self.fields[field_name].help_text = ''


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
