# coding=utf-8
'''Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça o usuario tentar adivinhar qual foi o numero escolhido pelo pc
 O Programa devera escrever na tela se o usuario venceu ou perder'''

from random import randint
from  time import sleep
cpu = randint(0,10) # Faz o computador "PENSAR"
print('= ' *  30)
print('Vou Analisar seu Pensamentos entre 0 e 5 Tente Adivinhar...')
print('= ' *  30)
jogador = int(input('Em que Numero eu Pensei? ')) # Jogador tente Adivinhar. 
print('Processando...')
sleep(5)
if jogador == cpu:
    print('Parabens voce me venceu!')
else:
     print('Ganhei ! Eu Analisei o Numero {} e nao {}'.format(cpu,jogador))   
