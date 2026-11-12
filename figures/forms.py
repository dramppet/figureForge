
from django import forms

from .models import Figure

class FigureForm(forms.ModelForm):
    class Meta:
        model = Figure
        fields = [
            'title',
            'character_name',
            'base_price',
            'height',
            'manufacturers',
            'materials',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'character_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'base_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'manufacturers': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class FigureDeleteForm(FigureForm):
    class Meta(FigureForm.Meta):
        model = Figure

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True
            field.required = False
