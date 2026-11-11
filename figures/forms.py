
from django import forms

from .models import Figure
from materials.choices import MaterialChoices


class FigureForm(forms.ModelForm):
    materials = forms.MultipleChoiceField(
        choices=MaterialChoices.choices,
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control'}
        ),
        required=True,
        label='Materials'
    )
    class Meta:
        model = Figure
        exclude = ['slug']

        labels = {
            'title': 'Title',
            'character_name': 'Character Name',
            'base_price': 'Base Price',
            'height': 'Height (cm)',
            'image_url': 'Image URL',
            'manufacturers': 'Manufacturer',
            'materials': 'Materials',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter figure title',
                'class': 'form-control',
            }),
            'character_name': forms.TextInput(attrs={
                'placeholder': 'Enter character name',
                'class': 'form-control',
            }),
            'base_price': forms.NumberInput(attrs={
                'placeholder': 'Enter base price',
                'class': 'form-control',
                'step': '0.01',
            }),
            'height': forms.NumberInput(attrs={
                'placeholder': 'Enter height in cm',
                'class': 'form-control',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Enter image URL',
                'class': 'form-control',
            }),
            'manufacturers': forms.Select(attrs={
                'class': 'form-control',
            }),
            'materials': forms.RadioSelect(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.setdefault(
                'class',
                'form-control'
            )
            field.error_messages['required'] = (
                'This field is required.'
            )

    def clean_title(self):
        value = self.cleaned_data['title'].strip()

        if len(value) < 3:
            raise forms.ValidationError(
                'The title must contain at least 3 characters.'
            )

        return value
