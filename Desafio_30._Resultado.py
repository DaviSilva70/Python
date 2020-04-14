'''Crie um peograma que leia um numero inteiro e mostre na tela se e impart ou par.'''


numero = int(input('Digite um número para saber se é Par ou Impar:'))
resto = numero % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')