from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('lk', views.lk, name='lk'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]
