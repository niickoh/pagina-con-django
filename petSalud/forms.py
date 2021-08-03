from django import forms
from .models import Login, Producto

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        
        
        