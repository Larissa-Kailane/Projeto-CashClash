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
            },
            {
                'text': 'O que é um orçamento familiar?',
                'option_a': 'Uma lista de compras do supermercado',
                'option_b': 'Um controle de todas as receitas e despesas da família',
                'option_c': 'O dinheiro guardado no banco',
                'option_d': 'As dívidas que precisam ser pagas',
                'correct_option': 'B',
                'explanation': 'Um orçamento familiar é um planejamento financeiro que registra e controla todas as entradas (receitas) e saídas (despesas) de dinheiro da família, ajudando a organizar as finanças.'
            },
            {
                'text': 'Qual é a diferença entre necessidade e desejo?',
                'option_a': 'Necessidade é mais barato, desejo é mais caro',
                'option_b': 'Necessidade é para adultos, desejo é para crianças',
                'option_c': 'Necessidade é essencial para viver, desejo é algo que queremos mas podemos viver sem',
                'option_d': 'Não há diferença, são a mesma coisa',
                'correct_option': 'C',
                'explanation': 'Necessidades são itens essenciais para nossa sobrevivência (como comida, moradia), enquanto desejos são coisas que gostaríamos de ter mas não são fundamentais. Entender essa diferença é crucial para boas decisões financeiras.'
            },
            {
                'text': 'O que significa ser um consumidor consciente?',
                'option_a': 'Comprar tudo que está em promoção',
                'option_b': 'Gastar todo o dinheiro que tem',
                'option_c': 'Pesquisar preços e comprar apenas o necessário',
                'option_d': 'Comprar apenas produtos caros',
                'correct_option': 'C',
                'explanation': 'Um consumidor consciente pesquisa preços, avalia a real necessidade da compra, compara produtos e marcas, e faz escolhas que respeitam seu orçamento e o meio ambiente.'
            },
            {
                'text': 'Qual é a melhor atitude ao receber mesada ou dinheiro de presente?',
                'option_a': 'Gastar tudo imediatamente em doces',
                'option_b': 'Guardar uma parte e usar outra parte para gastos planejados',
                'option_c': 'Emprestar todo o dinheiro para os amigos',
                'option_d': 'Esconder o dinheiro embaixo do colchão',
                'correct_option': 'B',
                'explanation': 'O ideal é desenvolver o hábito de poupar parte do dinheiro recebido e usar o restante de forma planejada, equilibrando economia e gastos responsáveis.'
            },
            {
                'text': 'Por que é importante comparar preços antes de comprar?',
                'option_a': 'Não é importante, devemos comprar no primeiro lugar',
                'option_b': 'Para gastar mais dinheiro',
                'option_c': 'Para encontrar o melhor custo-benefício',
                'option_d': 'Para demorar mais tempo comprando',
                'correct_option': 'C',
                'explanation': 'Comparar preços nos ajuda a encontrar o melhor custo-benefício, economizar dinheiro e fazer escolhas mais inteligentes de consumo.'
            },
            {
                'text': 'O que é um investimento?',
                'option_a': 'Gastar dinheiro em jogos',
                'option_b': 'Guardar dinheiro embaixo do colchão',
                'option_c': 'Aplicar dinheiro esperando receber mais no futuro',
                'option_d': 'Emprestar dinheiro para amigos',
                'correct_option': 'C',
                'explanation': 'Investimento é quando aplicamos dinheiro em algo (como poupança, ações, títulos) com a expectativa de receber um retorno maior no futuro, fazendo nosso dinheiro crescer.'
            },
            {
                'text': 'Como podemos economizar energia em casa?',
                'option_a': 'Deixando todas as luzes acesas',
                'option_b': 'Usando vários aparelhos ao mesmo tempo',
                'option_c': 'Apagando as luzes ao sair e usando aparelhos eficientes',
                'option_d': 'Nunca usando aparelhos elétricos',
                'correct_option': 'C',
                'explanation': 'Economizar energia inclui hábitos como apagar luzes em ambientes vazios, usar aparelhos eficientes e evitar desperdícios. Isso ajuda tanto o meio ambiente quanto o orçamento familiar.'
            },
            {
                'text': 'O que significa ser sustentável financeiramente?',
                'option_a': 'Gastar todo o dinheiro que ganha',
                'option_b': 'Nunca gastar dinheiro',
                'option_c': 'Manter equilíbrio entre ganhos, gastos e economia',
                'option_d': 'Pedir dinheiro emprestado sempre',
                'correct_option': 'C',
                'explanation': 'Ser sustentável financeiramente significa manter um equilíbrio saudável entre o que se ganha, o que se gasta e o que se guarda, garantindo estabilidade financeira a longo prazo.'
            },
            {
                'text': 'Por que é importante ter objetivos financeiros?',
                'option_a': 'Para gastar mais dinheiro',
                'option_b': 'Para impressionar os amigos',
                'option_c': 'Para planejar e realizar sonhos de forma organizada',
                'option_d': 'Para ficar mais rico que todos',
                'correct_option': 'C',
                'explanation': 'Objetivos financeiros nos ajudam a planejar nosso futuro, organizar nossas economias e realizar nossos sonhos de forma responsável e planejada.'
            },
            {
                'text': 'Como o uso do cartão de crédito afeta nosso orçamento?',
                'option_a': 'Não afeta, pois é dinheiro grátis',
                'option_b': 'É sempre melhor que dinheiro em espécie',
                'option_c': 'Pode gerar dívidas se não for usado com responsabilidade',
                'option_d': 'Só deve ser usado em emergências',
                'correct_option': 'C',
                'explanation': 'O cartão de crédito é uma forma de pagamento que pode gerar dívidas se não for usado com planejamento e responsabilidade, pois o dinheiro gasto precisa ser pago posteriormente, geralmente com juros.'
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