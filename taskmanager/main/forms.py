from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField


class regForm(UserCreationForm):
    username = forms.CharField(label='Логин',
        max_length=150, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    first_name = forms.CharField(label='Имя', max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(label='Фамилия', max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Пароль', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'type': 'password'}))
    password2 = forms.CharField(label='Подтверждение пароля', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'type': 'password'}))
    email = forms.CharField(label='Email', max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Пользователь с таким именем уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Такой E-mail уже используется")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")

        return password2
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        return user
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email')


class authoForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={"autofocus": True, 'class': 'form-control form-control-lg'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'class': 'form-control form-control-lg', 'type': 'password'}),
    )
    class Meta:
        model = User
        fields= ('username','password')