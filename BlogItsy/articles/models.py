from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Author(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    aboutme         = models.TextField(blank = True)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title           = models.CharField(max_length=100)
    slug            = models.SlugField()
    body            = models.TextField()
    image_1         = models.FileField(default='default.jpg', blank=True)
    image_2         = models.FileField(default='default.jpg', blank=True)
    image_3         = models.FileField(default='default.jpg', blank=True)
    date            = models.DateTimeField(auto_now_add=True)
    comment_count   = models.IntegerField(default=0)
    content         = HTMLField()
    author          = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured        = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Signup(models.Model):
    name        = models.CharField(max_length=100)
    email       = models.EmailField()
    message     = models.TextField(blank = True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
