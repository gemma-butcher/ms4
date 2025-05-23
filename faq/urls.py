from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('faq/', views.faq_list, name='faq'),
    path('', views.faq_list, name='faq_list'),
    path('add/', views.faq_add, name='faq_add'),
    path('<int:pk>/update/', views.faq_update, name='faq_update'),
    path('<int:pk>/delete/', views.faq_delete, name='faq_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
