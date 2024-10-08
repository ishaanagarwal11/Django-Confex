from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default1.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False) 
    pdf = models.FileField(upload_to='pdfs/', blank=True)
    # New fields
    email = models.EmailField()
    organization = models.CharField(max_length=255)

    def __str__(self):
        return self.title  

    def snippet(self):
        return self.body[:20] + '...'
