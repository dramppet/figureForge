
from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = [
            'author_name',
            'rating',
            'comment',
            'figure',
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

        for field in self.fields.values():
            field.widget.attrs.setdefault(
                'class',
                'form-control'
            )

            field.error_messages['required'] = (
                'Please fill out this field.'
            )
