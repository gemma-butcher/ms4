from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'created_on')
    list_filter = ('category', 'created_on')


admin.site.register(FAQ, FAQAdmin)
