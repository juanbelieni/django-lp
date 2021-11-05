from django.urls import path, include
import instagram2.views as ig_views

urlpatterns = [
    path('', ig_views.index, name="index"),
    path('perfil/', ig_views.perfil, name='perfil')
]