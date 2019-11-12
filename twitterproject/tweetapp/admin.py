from django.contrib import admin
from .models import User, Tweets
from django import forms

class UserAdminForm(forms.modelForm):
    def __init__(self,*args,**kwargs):
        super(UserAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        name = self.cleaned_data.get('user_name')
        if len(name) > 20:
            raise forms.ValidationError('name is too big', code='error')
        return self.cleaned_data

    def save(self,commit=True):
        return super(UserAdminForm,self).save(commit=commit)

class TweetsAdminForm(forms.modelForm):
    def __init__(self,*args,**kwargs):
        super(TweetsAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        name = self.cleaned_data.get('tweet_length')
        if len(name) > 140:
            raise forms.ValidationError('name is too big', code='error')
        return self.cleaned_data

    def save(self, commit=True):
        return super(TweetsAdminForm,self).save(commit=commit)




class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_name','user_location','date_of_birth','no_of_tweets',)



class TweetsAdmin(admin.ModelAdmin):
    list_display = ('time_of_tweet','date_of_tweet','tweet_length',)


admin.site.register(User, UserAdmin)
admin.site.register(Tweets, TweetsAdmin)

