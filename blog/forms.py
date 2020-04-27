from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class Postform(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title','content','category','image','status')