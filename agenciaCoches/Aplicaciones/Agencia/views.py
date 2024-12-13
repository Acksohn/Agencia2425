from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Ciudad
from .models import Propietario
from .models import Modelo
from .models import Vehiculo

# Create your views here.
def home(request):
    return render(request,"home.html")

#CRUD PROPIETARIO
def listadoPropietarios(request):
    propietariosBdd=Propietario.objects.all()
    return render(request,"listadoPropietarios.html", {'propietarios':propietariosBdd})

def nuevoPropietario(request):
    ciudad = Ciudad.objects.all()
    return render(request,'nuevoPropietario.html', {'ciudads':ciudad })

def guardarPropietario(request):
    nom=request.POST["nombre"]
    ape=request.POST["apellido"]
    ema=request.POST["email"]
    tel=request.POST["telefono"]
    ciu=request.POST["ciudad"]
    ciudad_instancia=Ciudad.objects.get(id=ciu)
    nuevoPropietario=Propietario.objects.create(nombre=nom,apellido=ape,email=ema,telefono=tel,ciudad=ciudad_instancia)
    return redirect('listadoPropietarios')


def eliminarPropietario(request,id):
    propietarioEliminar=Propietario.objects.get(id=id)
    propietarioEliminar.delete()
    messages.success(request,"Propietario eliminado exitosamente")
    return redirect('listadoPropietarios')

def editarPropietario(request,id):
    propietarioEditar=Propietario.objects.get(id=id)
    ciudad = Ciudad.objects.all()
    return render(request,'editarPropietario.html',{'propietarioEditar':propietarioEditar, 'ciudads':ciudad})

def ActualizacionPropietario(request):
    id=request.POST['id']
    nom=request.POST["nombre"]
    ape=request.POST["apellido"]
    ema=request.POST["email"]
    tel=request.POST["telefono"]
    ciu=request.POST["ciudad"]
    ciudad_instancia=Ciudad.objects.get(id=ciu)
    propietarioConsultado=Propietario.objects.get(id=id)
    propietarioConsultado.nombre=nom
    propietarioConsultado.apellido=ape
    propietarioConsultado.email=ema
    propietarioConsultado.telefono=tel
    propietarioConsultado.ciudad=ciudad_instancia
    propietarioConsultado.save()
    messages.success(request,'Propietario actualizado exitosamente.')
    return redirect('listadoPropietarios')


#CRUD VEHICULO
def listadoVehiculos(request):
    vehiculosBdd=Vehiculo.objects.all()
    return render(request,"listadoVehiculos.html", {'vehiculos':vehiculosBdd})

def nuevoVehiculo(request):
    propietario = Propietario.objects.all()
    modelo = Modelo.objects.all()
    return render(request,'nuevoVehiculo.html', {'propietarios':propietario, 'modelos':modelo})

def guardarVehiculo(request):
    fab=request.POST["fabricacion"]
    pre=request.POST["precio"]
    pla=request.POST["placa"]
    mod=request.POST["modelo"]
    modelo_instancia=Modelo.objects.get(id=mod)
    pro=request.POST["propietario"]
    propietario_instancia=Propietario.objects.get(id=pro)
    nuevoVehiculo=Vehiculo.objects.create(fabricacion=fab,precio=pre,placa=pla,modelo=modelo_instancia,propietario=propietario_instancia)
    return redirect('listadoVehiculos')


def eliminarVehiculo(request,id):
    vehiculoEliminar=Vehiculo.objects.get(id=id)
    vehiculoEliminar.delete()
    messages.success(request,"Vehiculo eliminado exitosamente")
    return redirect('listadoVehiculos')

def editarVehiculo(request,id):
    vehiculoEditar=Vehiculo.objects.get(id=id)
    propietario = Propietario.objects.all()
    modelo = Modelo.objects.all()
    return render(request,'editarVehiculo.html',{'vehiculoEditar':vehiculoEditar, 'propietarios':propietario, 'modelos':modelo})

def ActualizacionVehiculo(request):
    id=request.POST['id']
    fab=request.POST["fabricacion"]
    pre=request.POST["precio"]
    pla=request.POST["placa"]
    mod=request.POST["modelo"]
    modelo_instancia=Modelo.objects.get(id=mod)
    pro=request.POST["propietario"]
    propietario_instancia=Propietario.objects.get(id=pro)
    vehiculoConsultado=Vehiculo.objects.get(id=id)
    vehiculoConsultado.fabricacion=fab
    vehiculoConsultado.precio=pre
    vehiculoConsultado.placa=pla
    vehiculoConsultado.modelo=modelo_instancia
    vehiculoConsultado.propietario=propietario_instancia
    vehiculoConsultado.save()
    messages.success(request,'Vehiculo actualizado exitosamente.')
    return redirect('listadoVehiculos')



#CRUD MODELO
def listadoModelos(request):
    modeloBdd=Modelo.objects.all()
    return render(request,"listadoModelos.html", {'modelos':modeloBdd})

def nuevoModelo(request):
    return render(request,'nuevoModelo.html', {})

def guardarModelo(request):
    nom=request.POST["nombre"]
    nuevoModelo=Modelo.objects.create(nombre=nom)
    return redirect('listadoModelos')


def eliminarModelo(request,id):
    modeloEliminar=Modelo.objects.get(id=id)
    modeloEliminar.delete()
    messages.success(request,"Modelo eliminado exitosamente")
    return redirect('listadoModelos')

def editarModelo(request,id):
    modeloEditar=Modelo.objects.get(id=id)
    return render(request,'editarModelo.html',{'modeloEditar':modeloEditar})

def ActualizacionModelo(request):
    id=request.POST['id']
    nom=request.POST["nombre"]
    modeloConsultado=Modelo.objects.get(id=id)
    modeloConsultado.nombre=nom
    modeloConsultado.save()
    messages.success(request,'Modelo actualizado exitosamente.')
    return redirect('listadoModelos')


#CRUD CIUDAD
def listadoCiudades(request):
    ciudadBdd=Ciudad.objects.all()
    return render(request,"listadoCiudades.html", {'ciudads':ciudadBdd})

def nuevoCiudad(request):
    return render(request,'nuevoCiudad.html', {})

def guardarCiudad(request):
    nom=request.POST["nombre"]
    nuevoCiudad=Ciudad.objects.create(nombre=nom)
    return redirect('listadoCiudades')


def eliminarCiudad(request,id):
    ciudadEliminar=Ciudad.objects.get(id=id)
    ciudadEliminar.delete()
    messages.success(request,"Ciudad eliminado exitosamente")
    return redirect('listadoCiudades')

def editarCiudad(request,id):
    ciudadEditar=Ciudad.objects.get(id=id)
    return render(request,'editarCiudad.html',{'ciudadEditar':ciudadEditar})

def ActualizacionCiudad(request):
    id=request.POST['id']
    nom=request.POST["nombre"]
    ciudadConsultado=Ciudad.objects.get(id=id)
    ciudadConsultado.nombre=nom
    ciudadConsultado.save()
    messages.success(request,'Ciudad actualizada exitosamente.')
    return redirect('listadoCiudades')