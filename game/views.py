from django.shortcuts import render, redirect
from game.actions import GameActions

def tela_inicial(request):
    return render(request, "game/telaInicial.html")

def iniciar_jogo(request):
    GameActions.comecar_game()
    request.session.pop('explicacao', None)
    request.session.pop('resposta_correta_texto', None) # Atualizado para um nome mais descritivo
    request.session.pop('dica_da_pergunta', None) # Nova variável para a dica
    return redirect("tela_pergunta")


def tela_pergunta(request):
    game_state = GameActions.get_game_state()
    
    if game_state.finished:
        if game_state.position > 10:  # Vitória
            return redirect("tela_vitoria")
        else:  # Derrota
            return redirect("tela_derrota")
    
    if request.method == "POST":
        resposta_usuario = request.POST.get("resposta")
        
        # Obter a pergunta atual para acessar a resposta correta e a dica
        pergunta_atual = game_state.current_question 
        
        is_correct, full_explanation = GameActions.verificar_resposta(resposta_usuario) # Renomeado 'explanation' para 'full_explanation'

        if is_correct:
            # Armazena a explicação na sessão para usar na próxima tela
            request.session['explicacao'] = full_explanation
            request.session.pop('dica_da_pergunta', None)
            request.session.pop('resposta_correta_texto', None)
            return redirect("tela_resposta_correta")
        else:
            #Resposta incorreta
         #   game_state.lives -= 1
           # game_state.save()

            if pergunta_atual: # Verificação para evitar erro se pergunta_atual for None
                request.session['resposta_correta_texto'] = getattr(pergunta_atual, f'alternativa_{pergunta_atual.alternativa_correta.lower()}')
                request.session['dica_da_pergunta'] = pergunta_atual.dica
            
            else: # Fallback caso não haja pergunta (não deveria acontecer se o stage está ok)
                request.session['resposta_correta_texto'] = "Resposta não encontrada."
                request.session['dica_da_pergunta'] = "Dica não disponível."
            
            if game_state.lives <= 0:  # Game over
                # A tela de derrota usa 'casa_atual', já está sendo passada corretamente
                return redirect("tela_derrota")
            else:  # Ainda tem vidas
                return redirect("tela_vida_perdida")

    return render(request, "game/tela_perguntas.html", {
        "posicao": game_state.position,
        "vidas": game_state.lives,
        "pergunta": game_state.current_question
    })

def tela_vida_perdida(request):
    game_state = GameActions.get_game_state()
    
    # Recupera o texto da resposta correta e a dica da sessão
    # Usando .pop para remover da sessão após o uso, para não persistir para outras telas
    resposta_correta_texto = request.session.pop('resposta_correta_texto', 'N/A')
    dica_da_pergunta = request.session.pop('dica_da_pergunta', 'N/A')

    context = {
        "posicao": game_state.position, # Posição atual no tabuleiro
        "vidas": game_state.lives,     # Vidas restantes
        # Não passamos 'explicacao' nem 'resposta_correta' (literalmente) aqui
        # pois queremos controlar o que aparece
        "resposta_correta_texto": resposta_correta_texto, # O texto da resposta correta (para sua referência, mas não será exibido com a mensagem "Resposta incorreta!")
        "dica_da_pergunta": dica_da_pergunta # A dica a ser exibida
    }
    return render(request, "game/tela_vida_perdida.html", context)

def tela_vitoria(request):
    game_state = GameActions.get_game_state()
    return render(request, "game/tela_vitoria.html", {
        "vidas": game_state.lives
    })

def tela_derrota(request):
    game_state = GameActions.get_game_state()
    return render(request, "game/tela_derrota.html", {
        "casa_atual": game_state.position
    })

def tela_resposta_correta(request):
    game_state = GameActions.get_game_state()
    explicacao = request.session.pop('explicacao', '') # Usa .pop para limpar a sessão após o uso
    return render(request, "game/tela_resposta_correta.html", {
        "posicao": game_state.position,
        "vidas": game_state.lives,
        "explicacao": explicacao
    })
