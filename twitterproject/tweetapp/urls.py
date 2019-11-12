from .views import TweetsListAPIView, UserListAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'tweet/',TweetsListAPIView.as_view(), name='list-tweet'),
    url(r'user/',UserListAPIView.as_view(), name='list-user'),
]
