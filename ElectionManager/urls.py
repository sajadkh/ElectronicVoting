from . import views
from django.conf.urls import url, include

urlpatterns = [
    url('election', views.ElectionView.as_view()),
    url('vote', views.VoteView.as_view()),
    url('choices', views.ChoicesView.as_view()),
]
