from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import SubscriberForm


@require_POST
def subscribe(request):
    form = SubscriberForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Thank you for subscribing to our newsletter!'
        })
    else:
        errors = form.errors.get(
            'email', 'Error subscribing. Please try again.'
        )
        return JsonResponse({
            'success': False, 
            'message': errors
        })
