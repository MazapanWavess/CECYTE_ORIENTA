from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apoyo-academico/', views.apoyo_academico, name='apoyo_academico'),
    path('contact/', views.contact, name='contact'),
    path('orientacion-vocacional/', views.orientacion_vocacional, name='orientacion_vocacional'),
    path('reservar/', views.reservar, name='reservar'),
    path('salud-mental/', views.salud_mental, name='salud_mental'),
    path('servicios/', views.servicios, name='servicios'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('orientacion-vocacional/', views.orientacion_vocacional, name='orientacion_vocacional'),
    path('reservar/', views.agendar_servicio, name='reservar'),
    path('resultados/', views.resultados, name='resultados'),
]