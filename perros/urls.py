from django.contrib import admin
from django.urls import path

from perros.views import (
    PerroListView,PerroDetailView,PerroCreateView,PerroUpdateView,PerroDeleteView,sobre_mi,ComentarioPagina
)

urlpatterns = [
    path("perros/", PerroListView.as_view(), name="lista_perros"),
    path('perros/<int:pk>/', PerroDetailView.as_view(), name="ver_perro"),
    path('perros/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('crear-perro/', PerroCreateView.as_view(), name="crear_perro"),
    path('editar-perro/<int:pk>/', PerroUpdateView.as_view(), name="editar_perro"),
    path('eliminar-perro/<int:pk>/', PerroDeleteView.as_view(), name="eliminar_perro"),
    path('sobre_mi/',sobre_mi,name="sobre_mi"),
    
]