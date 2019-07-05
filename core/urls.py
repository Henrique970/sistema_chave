from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('mostrar_chaves/', mostrar_chaves),
    path('informacoes_chave/<int:id>/', informacoes_chave),
    path('mostrar_chaves_disponiveis/', mostrar_chaves_disponiveis),
    path('mostrar_chaves_indisponiveis/', mostrar_chaves_indisponiveis),
    path('pegar_chave/<int:id>/', pegar_chave, name='pegar_chave'),
    path('devolver_chave/<int:id>/', devolver_chave, name='devolver_chave'),
    path('historico_chave/', historico_chave),
]