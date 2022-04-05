from django import forms

class regForm(forms.Form):
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
