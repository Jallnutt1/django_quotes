from tkinter import CASCADE
from django.db import models

class QuoteManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['author']) < 3:
            errors['author'] = "The authors name must be longer than 3 characters"
        if len(postData['quote']) < 10:
            errors['quote'] = "The quote must be longer then 10 characters"
        return errors   

class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey('appLogin.User', related_name='quote', on_delete=models.CASCADE)
    likes = models.ManyToManyField('appLogin.User', related_name='quote_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
