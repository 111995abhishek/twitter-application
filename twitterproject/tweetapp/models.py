from django.db import models
from django import *
from django.db.models import CASCADE,DO_NOTHING


class User(models.Model):
    user_id = models.IntegerField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_location= models.CharField(max_length=200)
    date_of_birth = models.DateField()
    no_of_tweets = models.IntegerField(max_length=200)

    def __str__(self):

        return str(self.user_id)+""+str(self.user_name)+""+str(self.date_of_birth)+""+str(self.no_of_tweets)



class Tweets(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    time_of_tweet = models.TimeField()
    date_of_tweet = models.DateField()

    def __str__(self):

        return str(self.time_of_tweet)+""+str(self.date_of_tweet)



