# CS350-Project-1/play/urls.py

from django.urls import path
from .views import PlayView

urlpatterns = [
    path('<int:round>/', PlayView.as_view(), name='play-view'),
]
