from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added', 'is_active')
    list_filter = ('is_active', 'date_added')
    search_fields = ('email',)
    date_hierarchy = 'date_added'
