from sys import maxsize
from django.db import models

# Create your models here.


class Draft(models.Model):
    title = models.CharField(max_length=255, unique=True, help_text='title')
    content = models.TextField(help_text='content')
    author = models.CharField(
        max_length=255, help_text='author', null=True, blank=True)
    description = models.CharField(
        max_length=255, help_text='description', null=True, blank=True)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='create time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update at')

    class Meta:
        verbose_name = 'draft'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title
