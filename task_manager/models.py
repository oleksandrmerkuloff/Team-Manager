from django.db import models
from django.template.defaultfilters import slugify


class Task(models.Model):
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Title'
        )
    slug = models.SlugField(
        blank=True, null=False,
        verbose_name='Slug'
        )
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Note(models.Model):
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Title'
        )
    slug = models.SlugField(
        blank=True, null=False,
        verbose_name='Slug'
        )
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
