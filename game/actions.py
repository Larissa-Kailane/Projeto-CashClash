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
        game_state.current_question = GameActions.get_random_question()
        game_state.save()
        return game_state

    @staticmethod
    def get_random_question():
        """Seleciona uma pergunta aleatória do banco de dados."""
        questions = Question.objects.all()
        if questions.exists():
            return random.choice(questions)
        return None

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
        
        if is_correct:
            game_state.position += 1
            if game_state.position > 10:  # Vitória
                game_state.finished = True
            else:
                game_state.current_question = GameActions.get_random_question()
        else:
            game_state.lives -= 1
            if game_state.lives <= 0:  # Derrota
                game_state.finished = True
        
        game_state.save()
        return is_correct, game_state.current_question.explanation if is_correct else "Resposta incorreta. A resposta correta era: " + getattr(game_state.current_question, f'option_{game_state.current_question.correct_option.lower()}')

    @staticmethod
    def get_game_state():
        """Retorna o estado atual do jogo."""
        game_state, created = GameState.objects.get_or_create(pk=1)
        if created:
            game_state.current_question = GameActions.get_random_question()
            game_state.save()
        return game_state 