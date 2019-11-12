from rest_framework import serializers
from .models import User,Tweets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','user_name','user_location','date_of_birth','no_of_tweets',)


class TweetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweets
        fields = ('time_of_tweet','date_of_tweet','tweet_length',)



