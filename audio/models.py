from django.db import models


class Audio(models.Model):
    src = models.TextField(help_text='src', unique=True)
    description = models.CharField(
        max_length=255, help_text='description', null=True, blank=True)
    name = models.CharField(max_length=255, help_text='name')
    unique_name = models.CharField(max_length=255, help_text='unique name')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='create time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update at')

    class Meta:
        verbose_name = 'audio'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']

    def __str__(self):
        return self.name
