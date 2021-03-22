from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_dojo', views.processDojoForm),
    path('create_ninja', views.processNinjaForm),
    path('delete_instance/<int:dojo_id>', views.deleteInstance),
]