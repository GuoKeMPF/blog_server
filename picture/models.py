from django.db import models


class Picture(models.Model):
    src = models.TextField(help_text='src', unique=True)
    width = models.IntegerField(help_text='width', unique=False)
    height = models.IntegerField(help_text='height', unique=False)
    description = models.CharField(
        max_length=255, help_text='description', null=True, blank=True)
    name = models.CharField(max_length=255, help_text='name')
    unique_name = models.CharField(max_length=255, help_text='unique name')
    views = models.IntegerField(default=0, verbose_name="views")
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='create time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update at')

    class Meta:
        verbose_name = 'picture'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.name
