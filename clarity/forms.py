from django.contrib.auth.models import User
from django import forms
from .models import Info

class UserForm(forms.ModelForm):
    # hides the password
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['category', 'link']

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)