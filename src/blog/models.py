from django.db import models

from django.shortcuts import reverse


# Create your models here:
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Заголовок")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Слаг")
    body = models.TextField(blank=True, db_index=True, verbose_name="Содержание")
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
        
        
class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Слаг")
    
    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
    
    def __str__(self):
        return F'{self.title}' 
