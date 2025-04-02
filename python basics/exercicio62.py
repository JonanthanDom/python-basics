'''Desafio 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
 mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('='*20)
print('progressão aritmetica')
print('='*20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
print(termo, end=' ')
while cont < 10:
    termo = termo + razao
    print(termo, end=' ')
    cont += 1
print('Pausa')
contador = 1
while contador > 0:
    contador += 1
    cont2= int(input('\nQuantos termos você quer mostrar a mais? '))
    if cont2 == 0:
        contador =0
    while cont2 > 0:
        termo += razao
        print(termo, end =' ')
        cont2 -= 1
        cont += 1
    print('Pausa')
print('Progressão finalizada com {} termos mostrados'.format(cont))
print('=-'*20)
