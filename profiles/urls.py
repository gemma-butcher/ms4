from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile')
]
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]