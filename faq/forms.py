from django import forms
from .models import FAQ


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'category']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['category'].empty_label = (
                "Please select a category from the dropdown list"
            )
