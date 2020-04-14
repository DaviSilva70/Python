# coding=utf-8
# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos
 # alunos.
# Faça um programa que leia o nome dos quatro alunos a ordem sorteada
# _____________________________________________________________________________________________
# Primeiro Metodo.
import random
aluno1 = str(input('Prmeiro Aluno:  '))
aluno2 = str(input('Segundo Aluno:  '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno :  '))

lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print('A Ordem foi:')
print(lista)
 # _________________________________________________________________________________________

# Segundo Metodo.
from random import shuffle

aluno1 = str(input('Prmeiro Aluno:  '))
aluno2 = str(input('Segundo Aluno:  '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno :  '))

lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print('A Ordem foi: ')
print(lista)
 # ___________________________________________________________________________________________