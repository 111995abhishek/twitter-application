from django.contrib import admin
from .models import User, Tweets


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_name','user_location','date_of_birth','no_of_tweets',)



class TweetsAdmin(admin.ModelAdmin):
    list_display = ('time_of_tweet','date_of_tweet',)


admin.site.register(User,UserAdmin)
admin.site.register(Tweets,TweetsAdmin)

