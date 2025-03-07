from django.db import models
from django.contrib.auth.models import AbstractUser


class TestImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="test_uploads/")  # No need for a custom function

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('trainer', 'Trainer'),
        ('stadium_owner', 'Stadium Owner'),
    ]
    email =  models.EmailField(unique=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='user')
    profile_photo  = models.ImageField(upload_to='profile_photos/',default='https://fitarena.s3.amazonaws.com/test_uploads/profile-default.png')
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.username