from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-dark border-white text-white',
                'placeholder': 'Your email address',
                'aria-label': 'Your email address'
            })
        }
