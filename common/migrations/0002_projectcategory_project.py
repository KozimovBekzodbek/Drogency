# Generated by Django 5.0.7 on 2024-07-13 11:54

import ckeditor.fields
import django.utils.timezone
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
            ],
            options={
                'verbose_name': 'project category',
                'verbose_name_plural': 'project categories',
                'db_table': 'project_category',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('slug', models.SlugField(max_length=256, verbose_name='slug')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[1100, 700], upload_to='projects/%Y/%m', verbose_name='image')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('price', models.CharField(max_length=256, verbose_name='price')),
                ('client', models.CharField(max_length=256, verbose_name='client')),
                ('designer', models.CharField(max_length=256, verbose_name='designer')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('categories', models.ManyToManyField(related_name='projects', to='common.projectcategory', verbose_name='categories')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'project',
            },
        ),
    ]
