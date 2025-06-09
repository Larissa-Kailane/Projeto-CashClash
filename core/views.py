from django.shortcuts import render, redirect

def tela_inicial(request):
    return render(request, "core/telaInicial.html")

def iniciar_jogo(request):
    request.session["posicao"] = 1
    request.session["vidas"] = 3
    return redirect("telaPerguntas")

def tela_pergunta(request):
    posicao = request.session.get("posicao", 1)
    vidas = request.session.get("vidas", 3)

    pergunta = {
        "texto": f"Qual o valor final de R$100 a 10% ao ano por {posicao} ano(s)?",
        "alternativas": ["R$ 110", "R$ 120", "R$ 130", "R$ 140"],
        "correta": "R$ 110"
    }

    if request.method == "POST":
        resposta = request.POST.get("resposta")
        if resposta == pergunta["correta"]:
            request.session["posicao"] = posicao + 1
            request.session["acertou"] = True
        else:
            request.session["vidas"] = vidas - 1
            request.session["acertou"] = False
        return redirect("tela_feedback")

    return render(request, "core/tela_pergunta.html", {
        "posicao": posicao,
        "vidas": vidas,
        "pergunta": pergunta
    })

def tela_feedback(request):
    posicao = request.session.get("posicao", 1)
    vidas = request.session.get("vidas", 3)
    acertou = request.session.get("acertou", False)

    explicacao = (
        "Se você investe R$ 1.000,00 a uma taxa de 5% ao ano, após um ano terá R$50,00..."
    )

    return render(request, "core/tela_feedback.html", {
        "posicao": posicao,
        "vidas": vidas,
        "acertou": acertou,
        "explicacao": explicacao
    })
