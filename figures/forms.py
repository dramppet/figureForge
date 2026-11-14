
from django import forms

from .models import Figure
from django.utils.text import slugify

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
                'placeholder': 'Figure title',
            }),
            'character_name': forms.TextInput(attrs={
                'placeholder': 'Character name',
                'class': 'form-control',
            }),
            'base_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Price (e.g. 25.50)',
            }),
            'height': forms.NumberInput(attrs={
                'placeholder': 'Height in cm',
                'class': 'form-control',
            }),
            'manufacturers': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        character = cleaned_data.get('character_name')
        if title and character:
            candidate = slugify(f'{title} - {character}')
            duplicates = Figure.objects.filter(slug=candidate).exclude(pk=self.instance.pk)
            if duplicates.exists():
                self.add_error('title', 'A figure with this title and character already exists.')
        return cleaned_data


class FigureDeleteForm(FigureForm):
    class Meta(FigureForm.Meta):
        model = Figure

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True
            field.required = False
