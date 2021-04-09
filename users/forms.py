from django import forms

from mains.models import Post, PostType
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
        types = PostType.objects.all()
        typesArr = ['None']
        for type in types:
            typesArr.append(type.choices)
        DOMAIN_CHOICES = ['Hardware', 'Software']
        TYPE_CHOICES = ['paid', 'not-paid']

        fields = ['title', 'domain', 'type', 'description']
        title = forms.CharField(required=True)

        domain = forms.ChoiceField(required=True, choices=DOMAIN_CHOICES)
        type = forms.ChoiceField(required=True, choices=typesArr)
        description = forms.CharField(widget=forms.Textarea)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'id': 'idTitle'
            })}


class UpdatePost(forms.ModelForm):
    '''
    def __init__(self,param, *args, **kwargs):
        DOMAIN_CHOICES = ['Hardware', 'Software']
        TYPE_CHOICES = ['paid', 'not-paid']

        super(UpdatePost, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(widget=forms.TextInput(attrs={'value':param.get('title'), 'class': 'form-control','placeholder': 'Title', 'id': 'idTitle',}))
        #self.fields['domain'] = forms.ChoiceField(required=True, choices=DOMAIN_CHOICES)
        self.initial['domain'] = param.get('domain')
        self.initial['type'] = param.get('type')
        self.initial['description'] = param.get('description')
        #self.fields['description'] = forms.CharField(widget=forms.Textarea(attrs = {'value':param.get('description')}))
        #self.fields['type'] = forms.ChoiceField(required=True, choices=TYPE_CHOICES)

    '''
    class Meta:
        model = Post

        fields = ['title', 'domain', 'type', 'description']

        DOMAIN_CHOICES = ['Hardware', 'Software']
        TYPE_CHOICES = ['paid', 'not-paid']

        fields = ['title', 'domain', 'type', 'description']
        title = forms.CharField(required=True)

        domain = forms.ChoiceField(required=True, choices=DOMAIN_CHOICES,)
        type = forms.ChoiceField(required=True, choices=TYPE_CHOICES)
        description = forms.CharField(widget=forms.Textarea)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'id': 'idTitle',
                

            })}

class FilterPosts(forms.Form):

    class Meta:


        DOMAIN_CHOICES = ['None', 'Hardware', 'Software']
        TYPE_CHOICES = ['None', ' paid', 'not-paid']

        fields = ['domain', 'type']
        domain = forms.ChoiceField(widget=forms.Select, required=True, choices=DOMAIN_CHOICES )
        type = forms.ChoiceField(widget=forms.Select, required=True, choices=TYPE_CHOICES)