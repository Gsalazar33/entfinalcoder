from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.padre),
    path('inicio/',views.inicio, name="Inicio"),
    path('perros/',views.perro, name="Perros" ),
    path('gatos/',views.gato, name="Gatos" ),
    path('aves/',views.ave, name="Aves" ),
    path('buscar/',views.buscar,name="Busqueda"),
    
]
