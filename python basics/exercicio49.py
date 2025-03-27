#Desafio 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

numero = int(input('Digite um número para calcular a tabuada:'))
for i in range(0,11):
    print('{} x {} = {}'.format(numero, i, numero*i))