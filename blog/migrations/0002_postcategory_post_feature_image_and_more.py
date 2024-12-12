# Generated by Django 4.2.9 on 2024-12-11 21:53

import cloudinary.models
import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('color', colorfield.fields.ColorField(default='#000', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='feature_image',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Upload a feature image', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Custom description for SEO (max 160 characters)', max_length=160),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Custom title for SEO (max 60 characters)', max_length=60),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, help_text='Comma-separated tags (e.g., Django,Python,Web)', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='blog.postcategory'),
        ),
    ]