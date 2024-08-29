from . import views
from django.urls import path

urlpatterns = [
    path('ga_module/', views.ga_module, name='ga_module'),
]