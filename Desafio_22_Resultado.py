# coding=utf-8
# Crie um Programa que leia o nome completo de uma pessoa e mostre:

# O Nome com todas as Letras Maiusculas.
# O nome com todas as Letras minusculas.
# Quantos letras ao todo( sem considerar espaços.)
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu Nome : ')).strip()
print('Analisando o que voce Digitou ... ')
print('Seu nome em Maiusculos e {}'.format(nome.upper()))
print('Seu Nome em minusculo e {}'.format(nome.lower()))
print('Se Nome tem ao  {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu Primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa) 
print('Seu Primeiro e {} e ele tem {} letras '.format(separa[0], len(separa[0])))
