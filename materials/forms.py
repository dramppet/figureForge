from django import forms
from .models import Material
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name']
        labels = {field:field.replace('_',' ').capitalize() for field in fields}
        widgets ={
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Material Name',
                }),
        }
