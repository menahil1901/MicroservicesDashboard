from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the default User model

from dashboard.models import ServiceDependency


class ServiceDependencyForm(forms.ModelForm):
    class Meta:
        model = ServiceDependency
        fields = ['source_microservice', 'target_microservice', 'relationship']

class CustomUserCreationForm(UserCreationForm):
    admin_token = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User  # Use the default User model
        fields = ('username', 'email', 'password1', 'password2', 'admin_token')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']  # Exclude 'password' field
        widgets = {
            'password': forms.HiddenInput(),  # Hide the password field
        }