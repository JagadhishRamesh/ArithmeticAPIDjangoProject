from django.urls import path
from . import views

urlpatterns = [
    path('arithmetic/', views.arithmetic_view, name='arithmetic'),
]