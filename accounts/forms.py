from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFromWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = ("username","email")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("E-mail already registered")
        return email