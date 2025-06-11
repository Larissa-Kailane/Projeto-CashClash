from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    explanation = models.TextField()

    def __str__(self):
        return self.text

class GameState(models.Model):
    position = models.IntegerField(default=1)
    lives = models.IntegerField(default=3)
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    finished = models.BooleanField(default=False)
    answered_questions = models.ManyToManyField(Question, related_name='games_answered', blank=True)

    def __str__(self):
        return f"Posição: {self.position}, Vidas: {self.lives}"
