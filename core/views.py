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
        request.session["explanation"] = explanation
        request.session["acertou"] = is_correct
        return redirect("tela_feedback")

    return render(request, "telaPerguntas.html", {
        "posicao": game_state.position,
        "vidas": game_state.lives,
        "pergunta": {
            "texto": game_state.current_question.texto if game_state.current_question else "",
            "alternativas": [
                game_state.current_question.alternativa_a,
                game_state.current_question.alternativa_b,
                game_state.current_question.alternativa_c,
                game_state.current_question.alternativa_d
            ] if game_state.current_question else []
        }
    })

def tela_feedback(request):
    game_state = GameActions.get_game_state()
    acertou = request.session.get("acertou", False)
    explicacao = request.session.get("explanation", "")

    return render(request, "telaFeedback.html", {
        "posicao": game_state.position,
        "vidas": game_state.lives,
        "acertou": acertou,
        "explicacao": explicacao
    })

def tela_vitoria(request):
    return render(request, "tela_vitoria.html")

def tela_derrota(request):
    return render(request, "tela_derrota.html")
