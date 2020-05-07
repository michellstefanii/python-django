from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'placeholder':'Subject'}))