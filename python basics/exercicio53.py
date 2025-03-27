#Desafio 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:
# PÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# recebendo as frases, eliminando os espaços e separando os elementos
frase = input('Digite uma frase: ').upper()
lista_letras = [letra for letra in frase if letra != ' ']
lista_letras = ''.join(lista_letras)
#criando uma lista inversa para comparação
lista_inversa = lista_letras[::-1]
lista_inversa = ''.join(lista_inversa)
print('A frase {} inversa fica {}'.format(lista_letras, lista_inversa))
#comparando as duas listas
if lista_letras == lista_inversa:
    print('É um palindromo')
else:
    print('Não é um palindromo.')
