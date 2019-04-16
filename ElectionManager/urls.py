from . import views
from django.conf.urls import url, include

urlpatterns = [
    url('election', views.ElectionView.as_view()),
]
