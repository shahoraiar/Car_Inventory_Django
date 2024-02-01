from django.urls import path 
from CarSync_app import views

urlpatterns = [
    path('',views.home , name='home'),
    path('caradd/', views.add_car , name='caradd'),
    path('showcar/', views.show_car, name='showcar'),
]