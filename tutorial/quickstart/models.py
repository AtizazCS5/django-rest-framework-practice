from django.db import models

# Create your models here.

class Comment(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateField()

    def __str__(self):
        return self.username