from django.db import models

class Article(models.Model):
    #author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)