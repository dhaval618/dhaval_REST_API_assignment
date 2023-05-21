from django.db import models

# Create your models here.
class User(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=150)
    publisher = models.CharField(max_length=100)


    def __str__(self):
        return self.title
