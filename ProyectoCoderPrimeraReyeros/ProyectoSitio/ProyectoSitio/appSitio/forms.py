from django import forms

class MadreFormulario(forms.Form):
    nombre = forms.CharField(max_length = 50)
    edad = forms.IntegerField()
    peso = forms.FloatField()

class BebeFormulario(forms.Form):

    dia = forms.IntegerField()
    mes = forms.IntegerField()
    year = forms.IntegerField()

class SemanaFormulario(forms.Form):

    semana = forms.IntegerField()