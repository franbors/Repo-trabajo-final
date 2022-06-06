from django.contrib import admin
from django.urls import path, include
from ProyectoBase.views import index_view, facebook_view, twitter_view
from ProyectoBase.views import paquete_view, oferta_view, cliente_view, contacto_view

from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name = 'index_view'),
    path('paquetes/', paquete_view, name = 'paquete_view'),
    path('ofertas/', oferta_view, name = 'oferta_view'),
    path('clientes/', cliente_view, name = 'cliente_view'),
    path('contactos/', contacto_view, name = 'contacto_view'),
    path('facebook/', facebook_view, name = 'facebook_view'),
    path('twitter/', twitter_view, name = 'twitter_view'),
    path('admin/', admin.site.urls)    
]
