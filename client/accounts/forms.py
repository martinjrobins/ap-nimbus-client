from django import forms
from django.conf import settings
from django.contrib.auth import forms as auth_forms

from .emails import send_user_creation_email
from .models import User


class RegistrationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ('full_name', 'institution', 'email')
        help_texts = {
            'email': 'For recovering your password',
            'full_name': 'For addressing you',
            'institution': 'For our records',
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean(self):
        if settings.AP_PREDICT_LDAP:
            self.add_error(None, 'Registration is disabled when using LDAP')
        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            user.save()
            send_user_creation_email(user, self.request)
        return user


class MyAccountForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = User
        fields = ('email', 'institution', 'full_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
