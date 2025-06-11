from django.shortcuts import get_object_or_404
from .models import Question, GameState
import random

class GameActions:
    @staticmethod
    def start_game():
        """Inicia um novo jogo, criando ou resetando o estado."""
        game_state, created = GameState.objects.get_or_create(pk=1)
        game_state.position = 1
        game_state.lives = 3
        game_state.finished = False
        game_state.save()
        # Limpa as perguntas respondidas
        game_state.answered_questions.clear()
        # Seleciona primeira pergunta
        game_state.current_question = GameActions.get_random_question()
        game_state.save()
        return game_state

    @staticmethod
    def get_random_question():
        """Seleciona uma pergunta aleatória que ainda não foi respondida."""
        game_state = get_object_or_404(GameState, pk=1)
        
        # Pega todas as perguntas que ainda não foram respondidas
        available_questions = Question.objects.exclude(
            id__in=game_state.answered_questions.values_list('id', flat=True)
        )
        
        if not available_questions.exists():
            # Se todas as perguntas já foram usadas, retorna None
            # O jogo deve tratar esse caso como uma vitória
            return None
            
        return random.choice(available_questions)

    @staticmethod
    def check_answer(answer):
        """Verifica a resposta e atualiza o estado do jogo."""
        game_state = get_object_or_404(GameState, pk=1)
        
        if not game_state.current_question:
            return False, "Nenhuma pergunta atual"

        # Mapeia a resposta do usuário para a letra correspondente
        answer_map = {
            game_state.current_question.option_a: 'A',
            game_state.current_question.option_b: 'B',
            game_state.current_question.option_c: 'C',
            game_state.current_question.option_d: 'D'
        }

        user_answer = answer_map.get(answer, '')
        is_correct = user_answer == game_state.current_question.correct_option
        
        # Guarda a explicação da pergunta atual antes de qualquer atualização
        current_explanation = game_state.current_question.explanation if is_correct else f"Resposta incorreta. A resposta correta era: {getattr(game_state.current_question, f'option_{game_state.current_question.correct_option.lower()}')}"
        
        if is_correct:
            # Adiciona a pergunta atual à lista de respondidas
            game_state.answered_questions.add(game_state.current_question)
            
            game_state.position += 1
            if game_state.position > 10:  # Vitória
                game_state.finished = True
            else:
                game_state.current_question = GameActions.get_random_question()
                # Se não houver mais perguntas disponíveis, considera como vitória
                if game_state.current_question is None:
                    game_state.finished = True
                    game_state.position = 11  # Força posição de vitória
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
            game_state.current_question = GameActions.get_random_question()
            game_state.save()
        return game_state 