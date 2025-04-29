from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ
from .forms import FAQForm

import json
import os
from django.conf import settings

def faq_list(request):
    file_path = os.path.join(settings.BASE_DIR, 'faq', 'static', 'faq', 'faqs.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        faq_data = json.load(f)

    return render(request, 'faq/faq_list.html', {'faq_data': faq_data})


def faq_create(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'faq/faq_form.html', {'form': form})


def faq_update(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm(instance=faq)
    return render(request, 'faq/faq_form.html', {'form': form})


def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        faq.delete()
        return redirect('faq_list')
    return render(request, 'faq/faq_confirm_delete.html', {'faq': faq})
