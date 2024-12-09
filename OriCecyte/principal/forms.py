from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'grupo', 'servicio', 'fecha_hora', 'motivo', 'contacto']