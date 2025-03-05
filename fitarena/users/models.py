from django.db import models
from django.contrib.auth.models import AbstractUser


class TestImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="test_uploads/")  # No need for a custom function

    def __str__(self):
        return self.name