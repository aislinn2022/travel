
from django.urls import path

from templateapp import views

urlpatterns = [
    path('', views.demo, name='demo')
]