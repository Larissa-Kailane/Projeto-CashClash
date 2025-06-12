from django.shortcuts import render, redirect
from game.actions import GameActions

def tela_inicial(request):
    return render(request, "telaInicial.html")

def iniciar_jogo(request):
    GameActions.start_game()
    return redirect("tela_pergunta")

def tela_pergunta(request):
    game_state = GameActions.get_game_state()
    
    if game_state.finished:
        if game_state.position > 10:  # Vitória
            return redirect("tela_vitoria")
        else:  # Derrota
            return redirect("tela_derrota")
    
    if request.method == "POST":
        resposta = request.POST.get("resposta")
        is_correct, explanation = GameActions.check_answer(resposta)
        
        if is_correct:
            # Armazena a explicação na sessão para usar na próxima tela
            request.session['explicacao'] = explanation
            return redirect("tela_resposta_correta")
        else:
            if game_state.lives > 0:  # Ainda tem vidas
                request.session['explicacao'] = explanation
                request.session['resposta_correta'] = resposta
                return redirect("tela_vida_perdida")
            else:  # Game over
                return redirect("tela_derrota")

    return render(request, "telaPerguntas.html", {
        "posicao": game_state.position,
        "vidas": game_state.lives,
        "pergunta": game_state.current_question
    })

def tela_vida_perdida(request):
    game_state = GameActions.get_game_state()
    return render(request, "tela_vida_perdida.html", {
        "posicao": game_state.position,
        "vidas": game_state.lives,
        "explicacao": request.session.get('explicacao', ''),
        "resposta_correta": request.session.get('resposta_correta', '')
    })

def tela_vitoria(request):
    game_state = GameActions.get_game_state()
    return render(request, "tela_vitoria.html", {
        "vidas": game_state.lives
    })

def tela_derrota(request):
    game_state = GameActions.get_game_state()
    return render(request, "tela_derrota.html", {
        "casa_atual": game_state.position
    })

def tela_resposta_correta(request):
    game_state = GameActions.get_game_state()
    return render(request, "tela_resposta_correta.html", {
        "posicao": game_state.position,
        "vidas": game_state.lives,
        "explicacao": request.session.get('explicacao', '')
    })
