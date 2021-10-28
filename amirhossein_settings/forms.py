from django import forms
from django.core import validators

# ContactForm

class CreateContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شما'}),
        validators=[validators.MaxLengthValidator(30, 'نام و نام خانوادگی شما نمی تواند بیشتر از 30 کاراکتر باشد')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        validators=[validators.MaxLengthValidator(30, 'ایمیل شما نمی تواند بیشتر از 30 کاراکتر باشد')]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'}),
        validators=[validators.MaxLengthValidator(30, 'موضوع نمی تواند بیشتر 30 کاراکتر باشد')]
    )
    text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'پیام شما'}),
        validators=[validators.MaxLengthValidator(500, 'پیام شما نمی تواند بیشتر از 500 کاراکتر باشد')]
    )