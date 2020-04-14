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
                                                .filter(status='publicado')

class Post(models.Model):
    STATUS  =   (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    title  =   models.CharField(max_length=250)
    slug    =   models.SlugField(max_length=250)#http://site.com/noticias/campeonato-braisleiro-2020/01/02/2020
    author  =   models.ForeignKey(User,
                                    on_delete=models.CASCADE)
    content =   models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created =   models.DateTimeField(auto_now_add=True)
    changed =   models.DateTimeField(auto_now=True)
    status  =   models.CharField(max_length=10,
                                    choices=STATUS,
                                    default='rascunhos')
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
