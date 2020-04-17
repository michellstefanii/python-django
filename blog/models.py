from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                                .filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    created =   models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"
        ordering = ('-created',)

    def __str__(self):
        return self.name

    

class Post(models.Model):
    STATUS  =   (
        ('draft','draft'),
        ('published','Published'),
    )
    title  =   models.CharField(verbose_name="Title",max_length=250)
    slug    =   models.SlugField(max_length=250)
    author  =   models.ForeignKey(User,
                                    on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="get_post")
    image   =   models.ImageField(upload_to="blog",blank=True,null=True)
    content =   models.TextField(verbose_name="Content")
    published = models.DateTimeField(default=timezone.now)
    created =   models.DateTimeField(auto_now_add=True)
    changed =   models.DateTimeField(auto_now=True)
    status  =   models.CharField(max_length=10,
                                    choices=STATUS,
                                    default='drafts')
    objects = models.Manager()
    publish = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.pk])

    def get_absolute_url_delete(self):
        return reverse('post_delete', args=[self.pk])

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Post)
def insert_slug(sender,instance,**kawrgs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()
    


# Create your models here.
