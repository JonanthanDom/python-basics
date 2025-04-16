'''Programa LabCalc com menu de 5 opções para demosntração das fórmulas matemáticas para análises laboratoriais.'''
TEXTO = 'LABCALC'
print('=-='*20)
print(TEXTO.center(55))
print('=-='*20) #título de apresentação 
menu = 0
while menu != 4: #início do laço de repetição do programa com menu inicial.
    menu = int(input('''Escolha a operação a ser realizada:
        [ 1 ] Relação Albumina/Creatinina
        [ 2 ] Calculo FiO2
        [ 3 ] Proteina de 24h
        [ 4 ] sair do programa '''))
    if menu ==1: #Primeira funcionalidade: calculo da relação albumina / creatinina (urina)
        print('Relação Albumina creatinina')
        albumina = float(input('Resultado da albumina urinária: '))
        creatinina = float(input('Resultado da creatinina urinária: '))
        creatinina = creatinina * 10 # é preciso converter a unidade da creatinina,isso é feito multiplicando por 10.
        calculo = (albumina / creatinina) * 1000 #o calculo é feito dividindo o resultado da albumina pela creatinina e multiplicando por 1000 valores normais são inferires a 30mg/g
        print('O reaultado é: {:.2f} mg/g'.format(calculo))
        print('='*30)
    elif menu == 2: #Segunda funcionalidade: calculo de FiO2 (fração inspirada de oxigênio).
        print('Calculo de FiO2')
        o2 = int(input('Valor de O2 em litros (cateter nasal): '))
        fio2 = (o2 * 4) + 21 #o cálculo é realizado multiplicando o valor de oxigênio por 4 somando 21.
        print('o FiO2 é de {}%'.format(fio2))
        print('='*30)
    elif menu == 3: # terceira funcionalidade:  proteína de 24h (urina)
        print('Proteína de 24h')
        volume = float(input('Volume de urina de 24h: '))
        proteina = float(input('Resultado da proteína urinária: '))
        calculo = (volume * proteina) / 100 #O calculo é feito multiplicando o volume pelo resultado, em seguida divide por 100, valores normais são inferiores a 150mg
        print('O resultado da proteina de 24h é: {}mg'.format(calculo))
        print('='*30)
    elif menu == 4:
        print('finalizando... Estarei aqui quando precisar.')
    else:
        print('Opção inválida')
print('Fim do programa.')