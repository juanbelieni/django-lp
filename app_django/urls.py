from django.urls import path, include
import app_django.views as app_views

urlpatterns = [
    path('', app_views.index),
]
