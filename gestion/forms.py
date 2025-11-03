from django import forms
from .models import Proyecto, Tester, CasoPrueba

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TesterForm(forms.ModelForm):
    class Meta:
        model = Tester
        fields = '__all__'

class CasoPruebaForm(forms.ModelForm):
    class Meta:
        model = CasoPrueba
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows':3}),
            'precondiciones': forms.Textarea(attrs={'rows':3}),
            'datos_entrada': forms.Textarea(attrs={'rows':2}),
            'pasos_ejecutar': forms.Textarea(attrs={'rows':3}),
            'resultado_esperado': forms.Textarea(attrs={'rows':3}),
            'dependencias': forms.Textarea(attrs={'rows':2}),
            'notas': forms.Textarea(attrs={'rows':2}),
        }

class BuscarCasoForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False, label="Buscar Caso de Prueba")
