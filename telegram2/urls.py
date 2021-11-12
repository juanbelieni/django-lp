from django.urls import path, include
import telegram2.views as tlg2_views

urlpatterns = [
    path('', tlg2_views.index, name="index"),
    path('introducao/', tlg2_views.introducao, name='introduction'),
    path('post/', tlg2_views.redireciona_inicio, name='redirect-home'),
    path('post/<str:text>', tlg2_views.post, name='post'),
    path('visualizacao/', tlg2_views.visualizacao, name='visualization')
]
