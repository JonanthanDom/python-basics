'''Desafio 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
import random
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
print('=-=' *10, ' PEDRA PAPEL TESOURA', '=-='*10)
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
palpite = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sorteio = random.choice(lista)
print('='*40)
print('O computador jogou {}'.format(sorteio))
print('Você jogou {}'.format(lista[palpite]))
print("="*40)
if sorteio == lista[palpite]:
    print('EMPATE!!!')
elif sorteio == lista[0]:
    if lista[palpite] == lista[1]:
        print('Papel cobre pedra. \n você venceu!!!!')
    elif lista[palpite] == lista[2]:
        print('Pedra quebra tesoura. \n computador venceu!!!!')
elif sorteio == lista[1]:
    if lista[palpite] == lista[0]:
        print('Papel cobre pedra. \n computador venceu!!!')
    elif lista[palpite] == lista[2]:
        print('Tesoura corta papel. \n você venceu!!!')
elif sorteio == lista[2]:
    if lista[palpite] == lista[0]:
        print('Pedra quebra tesoura. \n você venceu!!!')
    elif lista[palpite] == lista[1]:
        print('tesoura corta papel. \n computador venceu!!!')
print('-='*10 , 'FIM', '-='*10)