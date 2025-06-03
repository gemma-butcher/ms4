from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Save to database
        Contact.objects.create(name=name, email=email)
        return render(request, 'contact/contact.html', {'success': True})
    return render(request, 'contact/contact.html')
