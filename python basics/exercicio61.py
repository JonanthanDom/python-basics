'''Desafio 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('='*20)
print('10 termos de uma PA')
print('='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
print(termo)
while cont < 10:
    termo = termo + razao
    print(termo)
    cont += 1
print('ACABOU')