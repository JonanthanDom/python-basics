# Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
ano_nascimento = int(input('Qual o ano que você nasceu?'))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
print('em {}  você terá {} anos'.format(ano_atual, idade))
if idade < 18:
    tempo_restante = 18 - idade
    print('você deverá se alistar daqui a {} anos'.format(tempo_restante))
    print('Seu alistamento será em {}'.format(ano_atual + tempo_restante))
elif idade > 18:
    tempo_restante = idade - 18
    print('Você passou do prazo de alistament a {} anos, compareça ao serviço militar!'.format(tempo_restante))
    print('Seu alistamento deveria ter sido em {}'.format(ano_atual - tempo_restante))
else:
    print('você deve se alistar imediatamente!')
