from django import forms
from .models import Compra

class compraForm(forms.ModelForm):
    
    class Meta:
        model = Compra
        fields = "__all__"
