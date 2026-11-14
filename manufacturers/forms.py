from django import forms

from manufacturers.models import Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

        labels = {
            'name': 'Manufacturer name',
            'country': 'Manufacturer country',
            'website': 'Manufacturer website',
        }

        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder': 'Enter manufacturer Name',
                'class':'form-control'
            }),
            'country' : forms.TextInput(attrs={
                'placeholder': 'Enter manufacturer country',
                'class':'form-control'
            }),
            'website' : forms.URLInput(attrs={
                'placeholder': 'Enter manufacturer website',
                'class':'form-control'
            })
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

