from django.urls import path
from . import views

urlpatterns = [
    path("", views.tela_inicial, name="telaInicial"),
    path("iniciar/", views.iniciar_jogo, name="iniciar_jogo"),
    path("pergunta/", views.tela_pergunta, name="telaPerguntas"),
    path("feedback/", views.tela_feedback, name="tela_feedback"),
]
