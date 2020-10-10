from django import forms

from mains.models import Post
from .models import MyUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'inputUsername'
            }),

            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'id': 'inputEmail'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'inputPassword'
            }),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'inputUsername'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'inputPassword'
            }),
        }


class CreatePost(forms.ModelForm):


    class Meta:
        model = Post

        DOMAIN_CHOICES = ['Hardware', 'Software']
        TYPE_CHOICES = ['paid', 'not-paid']

        fields = ['title', 'domain', 'type', 'description']
        title = forms.CharField(required=True)

        domain = forms.ChoiceField(required=True, choices = DOMAIN_CHOICES)
        type = forms.ChoiceField(required=True, choices=TYPE_CHOICES)
        description = forms.CharField(widget = forms.Textarea)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'id': 'idTitle'
            })}



