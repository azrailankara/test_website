from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
import re

def tr_slugify(text):
    tr_map = {
        'ı': 'i', 'İ': 'i',
        'ğ': 'g', 'Ğ': 'g',
        'ü': 'u', 'Ü': 'u',
        'ş': 's', 'Ş': 's',
        'ö': 'o', 'Ö': 'o',
        'ç': 'c', 'Ç': 'c',
    }
    
    for tr_char, eng_char in tr_map.items():
        text = text.replace(tr_char, eng_char)
    
    text = text.lower()
    text = slugify(text)
    return text

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = tr_slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:category_list', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

def post_image_path(instance, filename):
    # Dosya adını slug'a göre oluştur
    ext = filename.split('.')[-1]
    if instance.slug:
        new_filename = f"{instance.slug}.{ext}"
    else:
        new_filename = f"{tr_slugify(instance.title)}.{ext}"
    return f"blog_images/{new_filename}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    summary = models.TextField(max_length=500, help_text="Ana sayfada görünecek kısa özet")
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    image = models.ImageField(upload_to=post_image_path, blank=True, null=True, help_text="Blog yazısı için kapak resmi")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = tr_slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={
            'year': self.created_date.year,
            'month': str(self.created_date.month).zfill(2),
            'day': str(self.created_date.day).zfill(2),
            'slug': self.slug
        })

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
