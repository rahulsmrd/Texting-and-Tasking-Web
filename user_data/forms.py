from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from user_data.models import *
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta():
        fields = ('username','email','password1','password2')
        model=get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address'

class profile_form(forms.ModelForm):
    class Meta():
        model=profile
        fields=('picture', 'description',)

        widgets={
            'picture':forms.FileInput(attrs={
                'placeholder':'Picture',
            }),
            'description': forms.Textarea(attrs={
                'placeholder':'Description',
                'rows':3,
                'cols':50,
            }),
        }