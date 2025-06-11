from django.core.management.base import BaseCommand
from game.models import Question

class Command(BaseCommand):
    help = 'Remove todas as perguntas do banco de dados'

    def handle(self, *args, **kwargs):
        Question.objects.all().delete()
        self.stdout.write('Todas as perguntas foram removidas com sucesso!') 