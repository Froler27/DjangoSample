from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    body = models.TextField()
    username = models.CharField(max_length=128, default="匿名")

    def __str__(self):
        return self.body