from django.urls import path, include
import app_django.views as app_views

urlpatterns = [
    path("", app_views.index, name='agenda'),
    path("outros/", app_views.outros, name="outros"),
    path("faculdade/", app_views.facul, name="faculdade"),
    path("facul/", app_views.redirect_faculdade, name="facul"),
    path("fgv/", app_views.redirect_faculdade, name="fgv"),
    path("date/<int:day>", app_views.by_day, name="by_day"),
]

"""
urlpatterns = [
    path('inicio/', app_views.inicio, name='app_index'),
    path('dinamic/<int:id>', app_views.dinamic, name="app-dinamico")


    path("", views.index, name="ferias1"),
    path("ferias2/", views.ferias2, name="ferias2"),
    path("ferias3/", views.ferias3, name="ferias3"),
    path("ferias/", views.redirect_ferias, name="ferias"),
    path("date/<int:month>", views.by_month, name="by_month"),
]
"""
