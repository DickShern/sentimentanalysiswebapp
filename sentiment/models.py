from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.
class Review(models.Model):
    review = models.CharField(max_length=1000)
    sentiment = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        label = {0:'Negative', 1:'Neutral', 2:'Positive'}
        sentiment_word = label[self.sentiment]
        return u'%s - %s' % (self.review, sentiment_word)