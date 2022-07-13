from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Поста'
        verbose_name_plural = 'Посты'
        ordering = {'time_create', 'title'}

class Category (models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})