from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):     # <-- ModelForm, no Form
    class Meta:
        model = Producto                  # <-- Conecta al modelo
        fields = ['nombre', 'descripcion', 'precio']   # <-- Qué campos usar
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Vestido rojo'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
        }