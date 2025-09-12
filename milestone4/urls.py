from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('faq/', include('faq.urls')),
    path('contact/', include('contact.urls')),
    path('profiles/', include('profiles.urls')),
    path('newsletter/', include('newsletter.urls')),
    path(
        'services/',
        TemplateView.as_view(template_name="services.html"),
        name='services'
    ),
]

# Add debug URL patterns for development
if settings.DEBUG:
    from django.http import FileResponse, Http404
    from django.views.decorators.http import require_GET
    import os

    @require_GET
    def favicon(request):
        try:
            favicon_path = os.path.join(
                settings.BASE_DIR, 'static', 'img', 'favicon.ico'
            )
            return FileResponse(
                open(favicon_path, 'rb'),
                content_type='image/x-icon'
            )
        except FileNotFoundError:
            raise Http404("Favicon not found")

    urlpatterns += [
        path(
            '404/',
            TemplateView.as_view(template_name='404.html'),
            name='404_test'
        ),
        path('favicon.ico', favicon),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
