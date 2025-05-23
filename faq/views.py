from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ
from .forms import FAQForm
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
import json
import os


def faq_list(request):
    faqs = FAQ.objects.all().order_by('category')
    # Group by category if needed
    categories = {}
    for faq in faqs:
        categories.setdefault(faq.category, []).append(faq)
    faq_data = [{'category': cat, 'questions': qs} for cat, qs in categories.items()]
    return render(request, 'faq/faq_list.html', {'faq_data': faq_data})


def faq_add(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'faq/faq_add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def faq_update(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm(instance=faq)
    return render(request, 'faq/faq_form.html', {'form': form, 'faq': faq})


def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        faq.delete()
        return redirect('faq_list')
    return render(request, 'faq/faq_confirm_delete.html', {'faq': faq})
