from django.urls import path, include
import whatsapp_2.views as wpp2_views

urlpatterns = [
    path('', wpp2_views.index),
]
