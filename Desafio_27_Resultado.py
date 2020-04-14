# coding=utf-8
'''Faça um programa que lei o nome completo de uma pessoa ,mostrando em seguida,
   a primeira ea ultimo nome separadamente:
Ex: Ana Maria
1 = Ana
2 = Maria '''

n = str(input('Digite seu Nome Completo:')).strip()
nome = n.split()
print('Muito Prazer em te conhecer ! ')
print('Seu Primeiro nome e {}'.format(nome[0]))
print('Seu Ultimo nome e {}'.format(nome[len(nome)-1])) 


nome = str(input('Digite seu nome')).strip()
n = nome.split()
print('Ola Amigo (a) ')
print('Seu 1º Nome e {}'.format(nome[0]))
print('Seu Ultimo Nome e {}'.format(nome[len(nome)-1])) 
