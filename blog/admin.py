from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display    =   ('name','created','published')
    list_filter     =   ('name','created','published')
    date_hierarchy  =   'published'
    search_fields   =   ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display    =   ('title','author','published','status')
    list_filter     =   ('status','created','published','author')
    readonly_fields =   ('views_image',)
    raw_id_fields   =   ('author',)
    date_hierarchy  =   'published'
    search_fields   =   ('title','content')
    prepopulated_fields =   {'slug':('title',)}

    def views_image(self,obj):
        return obj.view_image
    views_image.short_description = "Image View"
# Register your models here.
