from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #Propietario
    path('listadoPropietarios/',views.listadoPropietarios, name='listadoPropietarios'),
    path('nuevoPropietario/', views.nuevoPropietario, name='nuevoPropietario'),
    path('guardarPropietario/',views.guardarPropietario, name='guardarPropietario'),    
    path('eliminarPropietario/<id>',views.eliminarPropietario, name='eliminarPropietario'),
    path('editarPropietario/<id>',views.editarPropietario, name='editarPropietario'),
    path('ActualizacionPropietario/',views.ActualizacionPropietario, name='ActualizacionPropietario'),
    #Vehiculo
    path('listadoVehiculos/',views.listadoVehiculos, name='listadoVehiculos'),
    path('nuevoVehiculo/', views.nuevoVehiculo, name='nuevoVehiculo'),
    path('guardarVehiculo/',views.guardarVehiculo, name='guardarVehiculo'),    
    path('eliminarVehiculo/<id>',views.eliminarVehiculo, name='eliminarVehiculo'),
    path('editarVehiculo/<id>',views.editarVehiculo, name='editarVehiculo'),
    path('ActualizacionVehiculo/',views.ActualizacionVehiculo, name='ActualizacionVehiculo'),
    #Modelo
    path('listadoModelos/',views.listadoModelos, name='listadoModelos'),
    path('nuevoModelo/', views.nuevoModelo, name='nuevoModelo'),
    path('guardarModelo/',views.guardarModelo, name='guardarModelo'),    
    path('eliminarModelo/<id>',views.eliminarModelo, name='eliminarModelo'),
    path('editarModelo/<id>',views.editarModelo, name='editarModelo'),
    path('ActualizacionModelo/',views.ActualizacionModelo, name='ActualizacionModelo'),
    #Ciudad
    path('listadoCiudades/',views.listadoCiudades, name='listadoCiudades'),
    path('nuevoCiudad/', views.nuevoCiudad, name='nuevoCiudad'),
    path('guardarCiudad/',views.guardarCiudad, name='guardarCiudad'),    
    path('eliminarCiudad/<id>',views.eliminarCiudad, name='eliminarCiudad'),
    path('editarCiudad/<id>',views.editarCiudad, name='editarCiudad'),
    path('ActualizacionCiudad/',views.ActualizacionCiudad, name='ActualizacionCiudad'),
]