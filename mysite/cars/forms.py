from django import forms
from .models import Review
from django.forms import ModelForm

 
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" #Pasar todos los campos del modelo como campos del formulario.

        labels = {
            'first_name':"TU PRIMER NOMBRE",
            'last_name':"TU APELLIDO",
            'stars':"PUNTUACIÓN"
        }

        error_messages = {
            'stars':{
                'min_value': "El valor no puede ser menor a 0",
                'max_value': "El valor máximo no puede ser mayor a 5"
            }
        }