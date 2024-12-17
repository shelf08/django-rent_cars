from django.urls import path
from . import views


urlpatterns = [
    path('', views.tables_home, name='tables_home'),
    path('auto_home', views.car_list, name='auto_home'),
    path('lk', views.lk_view, name='lk'),
    path('signin/<str:name>/<str:phone_number>/', views.signin_view, name='signin'),
    path('signup', views.signup_view, name='signup'),
]