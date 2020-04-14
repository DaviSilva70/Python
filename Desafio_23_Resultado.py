# coding=utf-8
'''Faça um programa que leia um numero de 0 a 9999.

Ex: Digita um numero :1834

unidade: 4
dezena:3
centena:8
milhar:1 '''

# Primeiro Metodo.
numero =int(input('Informe um Numero: '))
n = str(numero)
print('Analisando o Numero {}'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar : {}\n'.format(n[0]))

# Segundo Metodo.


numero =int(input('Informe um Numero: '))
unidade = numero // 1 % 10
dezena = numero //  10 % 10
centena = numero // 100 % 10
milhar = numero //  1000 % 10
print('Analisando o Numero {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar : {}'.format(milhar))