import re
from django import forms
from django.contrib.auth.models import Group, User
from events.forms import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm

class CustomRegistrationForm(StyledFormMixin, forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password1', 'confirm_password', 'email']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise forms.ValidationError("Email already exists")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        errors = []
        if len(password1) < 8:
            errors.append('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password1):
            errors.append('Password must include at least one uppercase letter.')
        if not re.search(r'[a-z]', password1):
            errors.append('Password must include at least one lowercase letter.')
        if not re.search(r'[0-9]', password1):
            errors.append('Password must include at least one number.')
        if not re.search(r'[@#$%^&+=]', password1):
            errors.append('Password must include at least one special character.')
        if errors:
            raise forms.ValidationError(errors)
        return password1
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('confirm_password')
        if password1 and confirm_password and password1 != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    

class LoginForm(StyledFormMixin, AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username...'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password...'
    }))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class createGroupForm(forms.Form):
    group_name = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.SelectMultiple(attrs={
        'placeholder': 'Enter group name...'
    }))