from django.urls import path, include
import appCleomar.views as appCleoViews

urlpatterns = [
    path('', appCleoViews.index, name='index'),
    path('elogio/', appCleoViews.elogio, name='elogio')
]