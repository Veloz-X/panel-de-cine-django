from django import forms
from .models import Pelicula
from django.forms.widgets import SelectDateWidget

class CrearPelicula(forms.Form):
    name = forms.CharField(label="Nombre de la pelicula", max_length=200, widget=forms.TextInput(attrs={'class': '-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'}) )
    img = forms.CharField(label="URL de imagen de la pelicula", max_length=200, widget=forms.TextInput(attrs={'class': '-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'}))

class CrearVenta(forms.Form):
    nombre = forms.CharField(label="Nombre de la pelicula", max_length=200, widget=forms.TextInput(attrs={'class': '-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md','placeholder': 'Joffre Veloz'}) )
    cedula = forms.CharField(label="URL de imagen de la pelicula", max_length=200, widget=forms.TextInput(attrs={'class': '-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md','placeholder': '09999999999'}))
    numeroEntradas = forms.ChoiceField(
        label="Número de entradas",
        choices=[(str(i), str(i)) for i in range(1, 11)],
        widget=forms.Select(attrs={'class': 'item-center  -full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'})
    )
    fecha = forms.DateField(label="Fecha", widget=SelectDateWidget(attrs={'class': ' p-2 rounded-md border border-[#e0e0e0] bg-white text-sm font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'}))
    pelicula = forms.ModelChoiceField(queryset=Pelicula.objects.all(), label="Película", widget=forms.Select(attrs={'class': ' rounded-md border border-[#e0e0e0] bg-white py-3 text-xs font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'}))
    entrada2x1 = forms.ChoiceField(label="¿Entrada 2x1?", choices=[(True, 'Sí'), (False, 'No')], widget=forms.RadioSelect(attrs={'class': 'flex items-center space-x-6 mx-auto'}))

    def save(self):
        data = self.cleaned_data
        pelicula_id = data['pelicula'].id