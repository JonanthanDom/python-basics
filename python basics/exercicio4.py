#crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
#informações sobre ele.


v = input('digite algo:')
print('O tipo primitivo desse valor é:', type(v))
print('é uma letra?', v.isalpha())
print('é um número?', v.isnumeric())
print('contém letras e números?', v.isalnum())
print('está em letras maiusculas?', v.isupper())
print('está em letras minpusculas?', v.islower())
print('Só tem espaços?', v.isspace())
print('Está capitalizado?', v.istitle())
