from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from . models import Post
from .forms import Postform
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def hello(request):
        return HttpResponse('Hello World')

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
        model = Post
        template_name = 'blog/post_detail.html'
        #context_object_name = 'custom'

class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
        model = Post
        template_name = 'blog/post_new.html'
        form_class = Postform
        success_message = "%(field)s was created successfully"

        def form_valid(self, form):
                obj = form.save(commit=False)
                obj.author = self.request.user
                obj.save()
                return super().form_valid(form)

        def get_success_message(self, cleaned_data):
                return self.success_message % dict(
                cleaned_data,
                field=self.object.title,
                ) 


class BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
        model = Post
        form_class = Postform
        template_name = 'blog/post_edit.html'
        #fields = ('title','content')
        success_message = "%(field)s was edited successfully"

        def form_valid(self, form):
                obj = form.save(commit=False)
                obj.author = self.request.user
                obj.save()
                return super().form_valid(form)       

        def get_success_message(self, cleaned_data):
                return self.success_message % dict(
                cleaned_data,
                field=self.object.title,
                )


class BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
        model = Post
        template_name = 'blog/post_delete.html'
        success_url = reverse_lazy('home')
        success_message = "Delete successfully"

        def delete(self, request, *args, **kwargs):
                messages.success(self.request,self.success_message)
                return super(BlogDeleteView,self).delete(request, *args, **kwargs)