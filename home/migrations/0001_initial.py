# Generated by Django 3.1 on 2020-11-02 01:33

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('keywords', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('minamount', models.IntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Mavjud', 'Mavjud'), ('Mavud emas', 'Mavjud Emas')], default='Mavjud', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('keywords', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('minamount', models.IntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Mavjud', 'Mavjud'), ('Mavud emas', 'Mavjud Emas')], default='Mavjud', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(max_length=255)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('Muhim', 'Muhim'), ('False', 'Mavjud emas')], default='True', max_length=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('keywords', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('minamount', models.IntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Mavjud', 'Mavjud'), ('Mavud emas', 'Mavjud Emas')], default='Mavjud', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=255)),
                ('rate', models.IntegerField(default=5)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('detail', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('slug', models.SlugField(unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Deals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.deals')),
                ('Drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.drinks')),
                ('Foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.foods')),
            ],
        ),
    ]
