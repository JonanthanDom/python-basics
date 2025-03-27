# Faça um programa que leia um nímero inteiro e mostre na tela o seu sucessor e o seu antecessor
n = int(input("digite um número:"))
a = n - 1
s = n + 1
print('O número digitado foi {}, seu antecessor é {} e seu sucesor é {}'.format(n, a, s))

#outra forma de fazer
n = int(input('Digite um número:'))
print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}')