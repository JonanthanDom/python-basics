#Desafio 26: Faça um programa que leia uma frase pelo teclado e 
# mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
a = frase.count('A')
print('A letra A aparece {} vezes na frase.'.format(a))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+ 1) ) #busca a posição da primeira letra A
print('A letra A aparece a ultima vez na posição: {}'.format(frase.rfind('A') +1 )) #busca a posição agora de tras pra frente.
