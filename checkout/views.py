from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty. Please add items to your bag before proceeding to checkout.")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RH5ZHQw5cQaxDjf0GULRTEmJkM8dYZ8h5gErqdrOJ4V8YmkNG2VehZV7XtT2GXSk4EwJLiwBs1aXZ7VDdHwNPqn00lnSlChjA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
