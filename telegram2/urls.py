
from django.urls import path, include
import telegram2.views as tlg2_views

urlpatterns = [
    path('', tlg2_views.index, name="index"),
    path('introducao/', tlg2_views.introducao, name='introducao'),
]
