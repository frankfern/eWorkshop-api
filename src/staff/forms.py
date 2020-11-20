from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import Staff
from django.conf import settings
from django.contrib.auth.models import Group


class BaseFrom():

    def __init__(self, *args, **kwargs):
        for item in self.fields:
            self.fields[item].widget.attrs.update({
                'class': 'form-control'
            })


class CreateUserForm(UserCreationForm, BaseFrom):

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        BaseFrom.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            self.save_m2m()
        return user

    class Meta:
        model = Staff
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'ci',
            'address',
            'phone',
            'phone2',
            'groups'
        ]


class ChangeUserForm(UserChangeForm, BaseFrom):

    def __init__(self, *args, **kwargs):
        UserChangeForm.__init__(self, *args, **kwargs)
        BaseFrom.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            self.save_m2m()
        return user

    class Meta:
        model = Staff
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'ci',
            'address',
            'phone',
            'phone2',
        ]
