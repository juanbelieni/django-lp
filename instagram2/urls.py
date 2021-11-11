from django.urls import path, include
import instagram2.views as ig_views

urlpatterns = [
    path('', ig_views.index, name="index"),
    path('perfil/', ig_views.perfil, name='perfil'),
    path('perfil/', ig_views.redirect_to_perfil, name='perfil-redirect'),
    path('profile/<str:param>', ig_views.profile, name='perfil'),
    path('tiorafa/', ig_views.tiorafa, name='tiorafa')
]