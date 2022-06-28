from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *


# Create your views here.

def padre(request):
    return render(request,"Appcoder/padre.html")
    
def inicio(request):
    return render(request,"AppCoder/inicio.html")

def perro(request):
    if request.method=='POST':
        miFormulario=PerroFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            perro=Perro(name=informacion['name'],raza=informacion['raza'],edad=informacion['edad'])
            perro.save()
            return render(request,"AppCoder/padre.html")
    else:
        miFormulario=PerroFormulario()

    return render(request,"AppCoder/perros.html",{"miFormulario":miFormulario})

def gato(request):
    if request.method=='POST':
        miFormulario=GatoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            gato=Gato(name=informacion['name'],raza=informacion['raza'],edad=informacion['edad'])
            gato.save()
            return render(request,"AppCoder/padre.html")
    else:
        miFormulario=GatoFormulario()

    return render(request,"AppCoder/gatos.html",{"miFormulario":miFormulario})
    

def ave(request):
    if request.method=='POST':
        miFormulario=AveFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            ave=Ave(name=informacion['name'],raza=informacion['raza'],edad=informacion['edad'])
            ave.save()
            return render(request,"AppCoder/padre.html")
    else:
        miFormulario=AveFormulario()

    return render(request,"AppCoder/ave.html",{"miFormulario":miFormulario})

def buscar(request):
    
      if  request.GET["name"]: #if request.method == 'Get':

          #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['name'] 
            
            perrobusq = Perro.objects.filter(camada__icontains=nombre)
            
            return render(request, "AppCoder/inicio.html", {"name":nombre})

      else: 

          respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})
        
