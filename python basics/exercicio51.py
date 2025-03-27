#Desafio 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

print('='*20)
print('10 termos de uma PA')
print('='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
print(termo)
for i in range(0,9):
    termo = termo + razao
    print(termo)
print('ACABOU')