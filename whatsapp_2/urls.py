from django.urls import path, include
import whatsapp_2.views as wpp2_views

urlpatterns = [
    path('', wpp2_views.index, name='index'),
    path('contacts/', wpp2_views.contacts, name='contacts'),
    path('profile/', wpp2_views.redirect_to_contacts, name='profile-redirect'),
    path('profile/<str:param>', wpp2_views.profile, name='profile'),
    path('secret/', wpp2_views.secret, name='secret')
]
