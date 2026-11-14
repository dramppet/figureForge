
from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = [
            'name',
            'email',
            'figure',
            'chose_material',
        ]

        labels = {
            field: field.replace('_', ' ').capitalize()
            for field in fields
        }

        widgets = {
            field: forms.TextInput(
                attrs={
                    'placeholder': 'Enter ' + field.replace('_', ' '),
                    'class': 'form-control',
                }
            )
            for field in fields
            if field in [
                'title',
                'character_name',
                'name',
                'country',
                'author_name',
                'email',
            ]
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status_order'] = forms.CharField(
            label='Status',
            initial='Pending',
            disabled=True,
            required=False,
            help_text='The status is set automatically.',
        )

        for field in self.fields.values():
            field.widget.attrs.setdefault(
                'class',
                'form-control'
            )

            field.error_messages['required'] = (
                'Please fill out this field.'
            )

    def clean(self):
        data = super().clean()

        figure = data.get('figure')
        material = data.get('chose_material')

        if figure and material:
            if not figure.materials.filter(
                pk=material.pk
            ).exists():
                self.add_error(
                    'chose_material',
                    'This material is not available '
                    'for the selected figure.'
                )

        return data
