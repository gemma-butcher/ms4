from django import forms

from allauth.usersessions.internal import flows

from django import template


class ManageUserSessionsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    def save(self, request):
        flows.sessions.end_other_sessions(request, request.user)

register = template.Library()

@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={'class': class_name})
