from django.urls import path
from . import views

urlpatterns = [
    path("", views.tela_inicial, name="telaInicial"),
    path("iniciar/", views.iniciar_jogo, name="iniciar_jogo"),
    path("pergunta/", views.tela_pergunta, name="tela_pergunta"),
    path("vida-perdida/", views.tela_vida_perdida, name="tela_vida_perdida"),
    path("vitoria/", views.tela_vitoria, name="tela_vitoria"),
    path("derrota/", views.tela_derrota, name="tela_derrota"),
]
