from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class customRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = ['name','email','phone','city','pin','state']
