from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    POST_CHOICES = (
        ('draft', 'Draft'),
        ('published', "Published"),
    )
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    post_status = models.CharField(
        max_length=10, choices=POST_CHOICES, default='draft')
    body = models.TextField()
    image = models.ImageField(upload_to='blog', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title
