

# Create your models here.
from django.db import models

from django.utils import timezone

from django.db import models

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(UserRegistration, on_delete=models.CASCADE,related_name='posts')  # ForeignKey to UserRegistration
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)  
    image=models.ImageField(upload_to="picture/", default='default.jpg')

    def __str__(self):
        return self.title

