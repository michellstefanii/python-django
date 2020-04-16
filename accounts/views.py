from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationFromWithEmail

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationFromWithEmail
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')