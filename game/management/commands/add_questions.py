from django.core.management.base import BaseCommand
from game.models import Question

class Command(BaseCommand):
    help = 'Adiciona perguntas iniciais ao banco de dados'

    def handle(self, *args, **kwargs):
        questions = [
            {
                'texto': 'O que é um orçamento?',
                'alternativa_a': 'Uma lista de compras do supermercado.',
                'alternativa_b': 'Um plano que controla ganhos e gastos',
                'alternativa_c': 'Uma conta no banco.',
                'alternativa_d': 'Um cartão de crédito',
                'alternativa_correta': 'B',
                'explicacao': 'Um orçamento é um plano financeiro que ajuda a controlar quanto dinheiro você recebe e quanto gasta, permitindo organizar melhor suas finanças',
                'dica': 'Pense em como você pode organizar seu dinheiro de forma planejada.',
                'stage': 1
            },
            {
                'texto': 'O que diferencia juros simples de compostos?',
                'alternativa_a': 'Os compostos rendem mais porque calculam juros sobre juros',
                'alternativa_b': 'Os simples rendem mais a longo prazo.',
                'alternativa_c': 'Os compostos não aplicam taxas',
                'alternativa_d': 'Os simples atualizam o capital mensalmente.',
                'alternativa_correta': 'A',
                'explicacao': 'Juros compostos capitalizam os juros, ou seja, o valor sobre o qual se calcula aumenta a cada período.',
                'dica': 'Pense na ideia de juros sobre juros.',
                'stage': 2
            },
            {
                'texto': 'O que significa poupar dinheiro?',
                'alternativa_a': 'Gastar todo o dinheiro que tem.',
                'alternativa_b': 'Pedir dinheiro emprestado.',
                'alternativa_c': 'Guardar uma parte do dinheiro para usar depois.',
                'alternativa_d': 'Doar todo o dinheiro.',
                'alternativa_correta': 'C',
                'explicacao': 'Poupar significa guardar uma parte do dinheiro que você recebe, em vez de gastar tudo. Isso ajuda a ter dinheiro para emergências ou para realizar sonhos no futuro.',
                'dica': 'Pense no que você pode fazer com o dinheiro no futuro se não gastar tudo agora.',
                'stage': 3
            },
            {
                'texto': 'O que significa capital, na matemática financeira?',
                'alternativa_a': 'A soma dos juros ao longo do tempo.',
                'alternativa_b': 'O valor pago ao final de uma aplicação.',
                'alternativa_c': 'A taxa de crescimento mensal.',
                'alternativa_d': 'O valor inicial investido ou emprestado.',
                'alternativa_correta': 'D',
                'explicacao': 'Capital é o valor inicial de uma operação financeira.',
                'dica': 'Pense no ponto de partida, o “começo da história"',
                'stage': 4
            },
            {
                'texto': 'Qual é o significado de taxa de juros?',
                'alternativa_a': 'O tempo necessário para dobrar o investimento.',
                'alternativa_b': 'O percentual aplicado sobre o capital ou montante.',
                'alternativa_c': 'O valor total final de uma aplicação.',
                'alternativa_d': 'O número de meses de aplicação.',
                'alternativa_correta': 'B',
                'explicacao': 'A taxa de juros representa quanto será aplicado (em %) sobre um valor para calcular o acréscimo.',
                'dica': 'Pense como um acréscimo sobre um valor',
                'stage': 5
            },
            {
                'texto': 'O que é inflação?',
                'alternativa_a': 'Quando os preços dos produtos diminuem.',
                'alternativa_b': 'Quando o dinheiro vale mais.',
                'alternativa_c': 'Quando os preços dos produtos aumentam.',
                'alternativa_d': 'Quando o salário aumenta.',
                'alternativa_correta': 'C',
                'explicacao': 'Inflação é o aumento geral dos preços dos produtos e serviços, fazendo com que o dinheiro perca seu poder de compra ao longo do tempo.',
                'dica': 'Imagine que o pão que você compra hoje custará mais ano que vem.',
                'stage': 6
            },
            {
                'texto': 'O que é um investimento?',
                'alternativa_a': 'Gastar dinheiro em jogos.',
                'alternativa_b': 'Guardar dinheiro no cofrinho.',
                'alternativa_c': 'Emprestar dinheiro para amigos.',
                'alternativa_d': 'Aplicar dinheiro esperando receber mais no futuro',
                'alternativa_correta': 'D',
                'explicacao': 'Investimento é quando aplicamos dinheiro em algo (como poupança, ações, títulos) com a expectativa de receber um retorno maior no futuro, fazendo nosso dinheiro crescer',
                'dica': 'Pense em fazer o seu dinheiro "trabalhar" para você.',                
                'stage': 7
            },
            {
                'texto': 'O que significa ser um consumidor consciente?',
                'alternativa_a': 'Pesquisar preços e comprar apenas o necessário.',
                'alternativa_b': 'Gastar todo o dinheiro que tem.',
                'alternativa_c': 'Comprar tudo que está em promoção.',
                'alternativa_d': 'Comprar apenas produtos caros.',
                'alternativa_correta': 'A',
                'explicacao': 'Um consumidor consciente pesquisa preços, avalia a real necessidade da compra, compara produtos e marcas, e faz escolhas que respeitam seu orçamento e o meio ambiente',
                'dica': 'Não é só sobre comprar, é sobre comprar bem e o que realmente precisa.',
                'stage': 8
            },
            {
                'texto': 'O que é montante em uma aplicação?',
                'alternativa_a': 'O valor pago em juros.',
                'alternativa_b': 'O valor final após aplicação de juros ao capital.',
                'alternativa_c': 'O valor inicial antes dos juros.',
                'alternativa_d': 'A taxa de correção monetária.',
                'alternativa_correta': 'B',
                'explicacao': 'Montante é a soma do capital + juros, ou seja, o valor total ao final da operação.',
                'dica': 'Pense em tudo o que você tem no fim',
                'stage': 9
            },
            {
                'texto': 'Por que é importante economizar dinheiro?',
                'alternativa_a': 'Para nunca gastar nada',
                'alternativa_b': 'Para ficar rico em um dia',
                'alternativa_c': 'Para comprar tudo que vê pela frente',
                'alternativa_d': 'Para ter segurança financeira e realizar objetivos',
                'alternativa_correta': 'D',
                'explicacao': 'Economizar é importante para ter segurança financeira em emergências e poder realizar seus objetivos futuros, como comprar algo especial ou investir em educação.',
                'dica': 'Pense em algo que você gostaria muito de ter ou fazer no futuro',
                'stage': 10
            }
        ]

        for question_data in questions:
            Question.objects.get_or_create(
                texto=question_data['texto'],
                defaults={
                    'alternativa_a': question_data['alternativa_a'],
                    'alternativa_b': question_data['alternativa_b'],
                    'alternativa_c': question_data['alternativa_c'],
                    'alternativa_d': question_data['alternativa_d'],
                    'alternativa_correta': question_data['alternativa_correta'],
                    'explicacao': question_data['explicacao'],
                    'dica': question_data['dica'],
                    'stage': question_data['stage']
                }
            )

        self.stdout.write(self.style.SUCCESS('Perguntas adicionadas com sucesso!')) 