from django.urls import path
from . import views

urlpatterns = [
    path('', views.tables_home, name='tables_home'),
]