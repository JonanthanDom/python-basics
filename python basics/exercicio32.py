#Desafio 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
from datetime import datetime
ano = int(input('Digite um ano para saber se ele é bissexto, ou digite 0 para o ano atual:'))
if ano == 0:
    ano = datetime.now().year
if calendar.isleap(ano):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'. format(ano))
