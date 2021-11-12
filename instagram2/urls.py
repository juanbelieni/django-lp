from django.urls import path, include
import instagram2.views as ig_views

urlpatterns = [
    path('', ig_views.index, name="index"),
    path('feed/', ig_views.feed, name='perfil'),
    path('feed/', ig_views.redirect_to_feed, name='perfil-redirect'),
    path('profile/<str:param>', ig_views.profile, name='perfil')
]