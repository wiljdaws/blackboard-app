from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        base_email = f"{user.first_name[0]}{user.last_name}@dallascollege.edu"
        email = base_email
        increment = 1

        while User.objects.filter(email=email).exists():
            email = f"{base_email}{increment}"
            # get everything before the @
            increment += 1

        user.email = email
        user.username = email.split('@')[0]

        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]