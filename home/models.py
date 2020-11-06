from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django.utils.safestring import mark_safe


# Create your models here.



class Foods(models.Model):
    STATUS = (
        ('Mavjud', 'Mavjud'),
        ('Mavud emas', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    keywords = models.CharField(max_length=50)
    detail = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='image/')
    price = models.IntegerField(blank=False)
    amount = models.IntegerField(blank=False)
    minamount = models.IntegerField(blank=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default='Mavjud')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="30">'.format(self.image.url))

    image_tag.short_description = 'Image'



class Drinks(models.Model):
    STATUS = (
        ('Mavjud', 'Mavjud'),
        ('Mavud emas', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    keywords = models.CharField(max_length=50)
    detail = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='image/')
    price = models.IntegerField(blank=False)
    amount = models.IntegerField(blank=False)
    minamount = models.IntegerField(blank=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default='Mavjud')

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="30">'.format(self.image.url))
    image_tag.short_description = 'Image'



class Deals(models.Model):
    STATUS = (
        ('Mavjud', 'Mavjud'),
        ('Mavud emas', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    keywords = models.CharField(max_length=50)
    detail = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='image/')
    price = models.IntegerField(blank=False)
    amount = models.IntegerField(blank=False)
    minamount = models.IntegerField(blank=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS, default='Mavjud')

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="30">'.format(self.image.url))
    image_tag.short_description = 'Image'


class Post(models.Model):
    comment = models.TextField(max_length=255, blank=True)
    rate = models.IntegerField(default=5)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    keywords = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=False)
    image = models.ImageField(blank=True, upload_to='image/')
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="30">'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    Deals = models.ForeignKey(Deals, on_delete=models.CASCADE)
    Drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE)
    Foods = models.ForeignKey(Foods, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class FAQ(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('Muhim', 'Muhim'),
        ('False', 'Mavjud emas'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=255)
    answer = RichTextUploadingField()
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question