from django.conf import settings

def free_shipping_threshold(request):
    return {
        'free_shipping_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }