from django.db import models

# Create your models here.

class Question(models.Model):
    texto = models.CharField(max_length=500)
    alternativa_a = models.CharField(max_length=200)
    alternativa_b = models.CharField(max_length=200)
    alternativa_c = models.CharField(max_length=200)
    alternativa_d = models.CharField(max_length=200)
    alternativa_correta = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    explicacao = models.TextField()  # Explicação para quando acertar
    dica = models.TextField(default="Pense bem sobre o conceito de educação financeira envolvido.")  # Dica para quando errar
    stage = models.IntegerField(default=1)  # Etapa em que a pergunta aparece (1 a 10)

    class Meta:
        ordering = ['stage']  # Ordena as perguntas por etapa

    def __str__(self):
        return f"Etapa {self.stage}: {self.texto[:50]}"

class GameState(models.Model):
    position = models.IntegerField(default=1)
    lives = models.IntegerField(default=3)
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    finished = models.BooleanField(default=False)
    answered_questions = models.ManyToManyField(Question, related_name='games_answered', blank=True)

    def __str__(self):
        return f"Posição: {self.position}, Vidas: {self.lives}"
