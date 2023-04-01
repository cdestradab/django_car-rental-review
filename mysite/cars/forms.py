from django import forms
from .models import Review
from django.forms import ModelForm

#Modelo de forma manual:
#class ReviewForm(forms.Form):
#    first_name = forms.CharField(label='First Name', max_length=100)
#    last_name = forms.CharField(label='Last Name', max_length=100)
#    email = forms.EmailField(label='E-Mail')
#    review = forms.CharField(label='Ingrese su comentario aquí', 
#                             widget=forms.Textarea(attrs={'class':'myform', 
#                                                          'rows':'2',
#                                                          'cols':'5'}))
 
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']