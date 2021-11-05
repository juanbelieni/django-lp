from django.urls import path, include
import app_django.views as app_views

urlpatterns = [
    path('', app_views.index, name='index'),
    path('app_index/', app_views.app_index, name='app_index'),
]
