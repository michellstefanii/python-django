# Generated by Django 3.0.5 on 2020-04-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200428_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='get_posts', to='blog.Category'),
        ),
    ]
