from django.shortcuts import get_object_or_404
from .models import Question, GameState
import random

class GameActions:
    @staticmethod
    def pegar_pergunta_para_casa(stage):
        """
        Retorna a pergunta específica para a etapa atual.
        """
        try:
            # Pega a primeira pergunta encontrada para a etapa
            return Question.objects.filter(stage=stage).first()
        except Question.DoesNotExist:
            return None

    @staticmethod
    def criar_game_state():
        """
        Cria um novo estado de jogo com valores iniciais.
        """
        game_state = GameState()
        game_state.position = 1
        game_state.lives = 3
        game_state.current_question = GameActions.pegar_pergunta_para_casa(1)
        game_state.save()
        return game_state

    @staticmethod
    def comecar_game():
        """
        Inicia um novo jogo.
        """
        # Limpa o estado anterior do jogo
        GameState.objects.all().delete()
        
        # Cria um novo estado de jogo
        game_state = GameActions.criar_game_state()
        game_state.finished = False
        game_state.save()
        return game_state


    @staticmethod
    def verificar_resposta(answer):
        """Verifica a resposta e atualiza o estado do jogo."""
        game_state = get_object_or_404(GameState, pk=1)
        
        if not game_state.current_question:
            return False, "Nenhuma pergunta atual"

        # Mapeia a resposta do usuário para a letra correspondente
        answer_map = {
            game_state.current_question.alternativa_a: 'A',
            game_state.current_question.alternativa_b: 'B',
            game_state.current_question.alternativa_c: 'C',
            game_state.current_question.alternativa_d: 'D'
        }

        user_answer = answer_map.get(answer, '')
        is_correct = user_answer == game_state.current_question.alternativa_correta
        
        # Guarda a explicação da pergunta atual
        current_explanation = game_state.current_question.explicacao if is_correct else f"Resposta incorreta. A resposta correta era: {getattr(game_state.current_question, f'alternativa_{game_state.current_question.alternativa_correta.lower()}')}"
        
        if is_correct:
            # Avança uma posição no tabuleiro
            game_state.position += 1
            
            # Verifica se chegou ao fim (após a casa 10)
            if game_state.position > 10:
                game_state.finished = True
            else:
                # Busca a pergunta da próxima etapa
                game_state.current_question = GameActions.pegar_pergunta_para_casa(game_state.position)
        else:
            game_state.lives -= 1
            if game_state.lives <= 0:  # Derrota
                game_state.finished = True
        
        game_state.save()
        return is_correct, current_explanation

    @staticmethod
    def get_game_state():
        """Retorna o estado atual do jogo."""
        game_state, created = GameState.objects.get_or_create(pk=1)
        if created:
            game_state.current_question = GameActions.pegar_pergunta_para_casa(1)
            game_state.save()
        return game_state 