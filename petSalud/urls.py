from django.urls import path
from petSalud.views import home, loginVista, registro, nuestros_productos, menu_gestion, descripcion, agregar,eliminar, listar_productos, modificar_producto, eliminar_producto



urlpatterns = [
    path('', home, name="home"),
    path('loginvista/', loginVista, name="loginvista"),
    path('registro/', registro, name="registro"),
    path('nuestros_productos/', nuestros_productos, name="nuestros_productos"),
    path('menu_gestion/', menu_gestion, name="menu_gestion"),
    path('descripcion/', descripcion, name="descripcion"),
    path('agregar/', agregar, name="agregar"),
    path('eliminar/', eliminar, name="eliminar"),
    path('listar/', listar_productos, name="listar_productos"),
    path('modificar/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar/<id>/', eliminar_producto, name="eliminar_producto"),
]