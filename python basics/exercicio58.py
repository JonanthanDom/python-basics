'''Desafio 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
num = randint(0, 10)
tentativas = 0
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar...')
print('-=-'*20)
palpite = int(input('Em qual número estou pensando?'))
tentativas += 1
while palpite != num:
    if palpite > num:
        print('Menos, tente mais uma vez')
        palpite = int(input('Qual o seu palpite? '))
        tentativas += 1
    if palpite < num:
        print('mais, tente mais uma vez')
        palpite = int(input('Qual o seu palpite? '))
        tentativas += 1
print('Acertou!!! com {} tentativas, o número escolhido foi {}'.format(tentativas, palpite))
