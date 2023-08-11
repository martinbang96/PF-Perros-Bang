from django import forms
from perros.models import Perro,Comentario
from PIL import Image
from django.contrib.auth.models import User

class PerroFormulario(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ('usuario','nombre', 'raza', 'edad', 'telefono', 'duenio', 'foto')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control','value':'','id':'usuario_id','type':'hidden'}),    
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }