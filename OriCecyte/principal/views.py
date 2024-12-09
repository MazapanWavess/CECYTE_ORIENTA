# Create your views here.

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def apoyo_academico(request):
    return render(request, 'ApoyoAcademico.html')

def contact(request):
    return render(request, 'contact.html')

def orientacion_vocacional(request):
    return render(request, 'orientacionVocacional.html')

def reservar(request):
    return render(request, 'reservar.html')

def salud_mental(request):
    return render(request, 'SaludMental.html')

def servicios(request):
    return render(request, 'servicios.html')

def sobre_nosotros(request):
    return render(request, 'SobreNosotros.html')


# Formulario 1

from django.shortcuts import render, redirect
from .forms import ReservaForm
from .models import Reserva

def agendar_servicio(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Guardar la reserva en la base de datos
            form.save()
            # Redirigir a una página de confirmación (resultados o gracias)
            return redirect('resultados')  # Asegúrate de crear esta vista
    else:
        form = ReservaForm()

    return render(request, 'reservar.html', {'form': form})

def resultados(request):
    # Mostrar todas las reservas
    reservas = Reserva.objects.all()
    return render(request, 'resultados.html', {'reservas': reservas})