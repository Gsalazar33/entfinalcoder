from django import forms

class PerroFormulario(forms.Form):
    name=forms.CharField()
    raza=forms.CharField()
    edad=forms.IntegerField()

class GatoFormulario(forms.Form):
    name=forms.CharField()
    raza=forms.CharField()
    edad=forms.IntegerField()

class AveFormulario(forms.Form):
    name=forms.CharField()
    raza=forms.CharField()
    edad=forms.IntegerField()