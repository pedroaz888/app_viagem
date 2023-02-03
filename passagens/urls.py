from django.urls import path
from . import views

urlpatterns =[
    path('index', views.index, name='index'),
    path('minha_consulta', views.revisao_consulta, name='minha_consulta'),

]