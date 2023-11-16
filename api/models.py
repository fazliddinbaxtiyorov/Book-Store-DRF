from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BookModels(models.Model):
    CATEGORY_CHOICES = (
        ('Classic', 'Classic'),
        ('Crime', 'Crime'),
        ('Horror', 'Horror'),
        ('Poetry', 'Poetry'),
        ('Romance', 'Romance'),
        ('Biography', 'Biography'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=120)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)
    published = models.DateField()
    iso = models.CharField(max_length=13)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)


class BlogPostSubscription(models.Model):
    email = models.EmailField(unique=True, max_length=100)

