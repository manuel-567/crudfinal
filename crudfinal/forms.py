from django import forms
from .models import Foto,Categoria

class PostFoto(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('Autor_Foto', 'Nombre_Foto','Descripcion_Foto','Archivo_Foto','Fecha_Foto','categoria')

def __init__ (self, *args, **kwargs):
        super(FotoForm, self).__init__(*args, **kwargs)
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["categoria"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["categoria"].help_text = "Ingrese los Actores que participaron en la película"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["categoria"].queryset = Actor.objects.all()

class PostCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('Nombre_Categoria','Descripcion_Categoria')
