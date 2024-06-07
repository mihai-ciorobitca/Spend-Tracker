# example/urls.py
from django.urls import path

from spendTracker.views import index


urlpatterns = [
    path('', index),
]