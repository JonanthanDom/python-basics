#Desafio 28:  Escreva um programa que faça o computador “pensar” em um número inteiro
#  entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#  O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
num = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*20)
palpite = int(input('Em qual número estou pensando?'))
print('PROCESSANDO...')
sleep(2) #faz o computador esperar antes de executar o próximo bloco
if palpite == num:
    print('Parabéns!!!!! o número foi {}'.format(num))
else:
    print('Errou!!!!!!! eu pensei em {}'. format(num))