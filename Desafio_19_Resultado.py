# coding=utf-8
# Um professor quer sortear um dos seus quadro alunos para apagar o quadro.Faça um programa que ajude
# ele lendo o nome deles a escrevendo o nome da escolhido.

# Primeiro Metodo 
import random
aluno1 = str(input('Digite o Nome do 1º Aluno: '))
aluno2 = str(input('Digite o Nome do 2º Aluno: ')) 
aluno3 = str(input('Digite o Nome do 3º Aluno: '))
aluno4 = str(input('Digite o Nome do 4º Aluno: '))

lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print('O Aluno Escolhido foi: {} \n'.format(escolhido))

# Segundo Metodo 

from random import choice
aluno1 = str(input('Digite o Nome do 1º Aluno: '))
aluno2 = str(input('Digite o Nome do 2º Aluno: ')) 
aluno3 = str(input('Digite o Nome do 3º Aluno: '))
aluno4 = str(input('Digite o Nome do 4º Aluno: '))

lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(lista)
print('O Aluno Escolhido foi: {} '.format(escolhido))
