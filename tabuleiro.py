from django.shortcuts import render

def tabuleiro(request):
    # Aqui você pode adicionar a lógica para carregar as perguntas do banco de dados
    # e gerenciar o estado do jogo
    context = {
        'vidas': 3,
        'posicao_atual': 0,
        # Adicione mais variáveis de contexto conforme necessário
    }
    return render(request, 'tela_inicial.html', context)
