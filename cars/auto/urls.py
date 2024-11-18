from django.urls import path
from . import views

urlpatterns = [
    path('', views.auto_home, name='auto_home'),
]