from django import forms
from django.forms import ModelForm
from .models import Users

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('fname','lname','uname','email','passwd')
        labels = {
            'fname': '',
            'lname': '',
            'uname': '',
            'email': '',
            'passwd': '',
        }
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control input-group', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control input-group', 'placeholder': 'Last Name'}),
            'uname': forms.TextInput(attrs={'class': 'form-control input-group', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control input-group', 'placeholder': 'Email'}),
            'passwd': forms.PasswordInput(attrs={'class': 'form-control input-group', 'placeholder': 'Password'}),
        }