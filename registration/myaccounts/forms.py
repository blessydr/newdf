from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author','image']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
