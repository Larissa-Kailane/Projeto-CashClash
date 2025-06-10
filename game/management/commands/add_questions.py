from django.core.management.base import BaseCommand
from game.models import Question

class Command(BaseCommand):
    help = 'Adiciona perguntas iniciais ao banco de dados'

    def handle(self, *args, **kwargs):
        questions = [
            {
                'text': 'Se você investe R$1.000,00 a uma taxa de 5% ao ano, quanto receberá de juros após um ano?',
                'option_a': 'R$ 50,00',
                'option_b': 'R$ 100,00',
                'option_c': 'R$ 150,00',
                'option_d': 'R$ 200,00',
                'correct_option': 'A',
                'explanation': 'Com juros simples de 5% ao ano, o valor dos juros é calculado multiplicando o capital (R$1.000,00) pela taxa (5% ou 0,05), resultando em R$50,00.'
            },
            {
                'text': 'O que são juros compostos?',
                'option_a': 'Juros que incidem apenas sobre o capital inicial',
                'option_b': 'Juros que incidem sobre o capital inicial e sobre os juros acumulados',
                'option_c': 'Juros que são pagos mensalmente',
                'option_d': 'Juros que são pagos apenas no final do investimento',
                'correct_option': 'B',
                'explanation': 'Juros compostos são aqueles que incidem não só sobre o capital inicial, mas também sobre os juros acumulados nos períodos anteriores, gerando um efeito de "bola de neve".'
            },
            {
                'text': 'Qual é a melhor forma de economizar dinheiro?',
                'option_a': 'Gastar todo o salário assim que receber',
                'option_b': 'Guardar o que sobrar no fim do mês',
                'option_c': 'Separar uma parte do dinheiro assim que receber',
                'option_d': 'Pedir dinheiro emprestado',
                'correct_option': 'C',
                'explanation': 'A melhor estratégia é separar uma parte do dinheiro assim que receber (poupar primeiro). Isso garante que você realmente economize, em vez de correr o risco de gastar tudo antes.'
            },
            {
                'text': 'O que é inflação?',
                'option_a': 'Quando os preços dos produtos diminuem',
                'option_b': 'Quando o dinheiro vale mais',
                'option_c': 'Quando os preços dos produtos aumentam',
                'option_d': 'Quando o salário aumenta',
                'correct_option': 'C',
                'explanation': 'Inflação é o aumento geral dos preços dos produtos e serviços, fazendo com que o dinheiro perca seu poder de compra ao longo do tempo.'
            },
            {
                'text': 'Por que é importante ter uma reserva de emergência?',
                'option_a': 'Para gastar em viagens',
                'option_b': 'Para comprar presentes',
                'option_c': 'Para estar preparado para imprevistos',
                'option_d': 'Para emprestar a amigos',
                'correct_option': 'C',
                'explanation': 'Uma reserva de emergência é importante para nos proteger de imprevistos financeiros, como problemas de saúde, desemprego ou despesas inesperadas, evitando que precisemos recorrer a empréstimos.'
            }
        ]

        for question_data in questions:
            Question.objects.get_or_create(
                text=question_data['text'],
                defaults={
                    'option_a': question_data['option_a'],
                    'option_b': question_data['option_b'],
                    'option_c': question_data['option_c'],
                    'option_d': question_data['option_d'],
                    'correct_option': question_data['correct_option'],
                    'explanation': question_data['explanation']
                }
            )

        self.stdout.write(self.style.SUCCESS('Perguntas adicionadas com sucesso!')) 