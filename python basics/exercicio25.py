#crie umn programa que leia um nome e diga se ela tem silva no nome:

name = input('Digite seu nome: ').strip()
name = name.upper()
name = name.split()
if "SILVA" in name: 
    print('Seu nome tem silva')
else:
    print('Seu nome não tem silva')

#refatorando:
name = input('Digite seu nome: ').strip()
print('Seu nome tem silva? {}'.format('silva' in name.lower()))